from django.shortcuts import render,redirect
from .models import Dog,Toy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import FeedingForm
from django.views.generic import ListView,DetailView


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request,'dogs/index.html',{
        'dogs':dogs
    })

def dogs_detail(request,dog_id):
    dog = Dog.objects.get(id=dog_id)

    current_toy_ids = dog.toys.all().values_list('id')
    available_toys = Toy.objects.exclude(id__in = current_toy_ids)

    feeding_form = FeedingForm()
    return render(request,'dogs/detail.html',{
        'dog':dog,'feeding_form':feeding_form,'available_toys':available_toys
    })


def add_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('detail', dog_id=dog_id)



def remove_toy(request, dog_id, toy_id):
    Dog.objects.get(id= dog_id).toys.remove(toy_id)
    return redirect('detail', dog_id=dog_id)

def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)


# Handle create and post request
class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    
    
class DogUpdate(UpdateView):
    model= Dog
    fields = ['breed','description','age']

class DogDelete(DeleteView):
    model= Dog
    success_url = '/dogs'


# Toy
class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model= Toy
    fields = "__all__"

class ToyDelete(DeleteView):
    model= Toy
    success_url = '/toys/'