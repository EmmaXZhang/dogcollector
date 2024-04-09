from django.shortcuts import render
from .models import Dog
from django.views.generic.edit import CreateView,UpdateView,DeleteView


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
    return render(request,'dogs/detail.html',{
        'dog':dog
    })

def add_feeding(request, cat_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)


# Handle create and post request
class DogCreate(CreateView):
    model = Dog
    # define fields = ["name","breed"] to be edit
    # all fields need to be edit
    fields = '__all__'
    
    
class DogUpdate(UpdateView):
    model= Dog
    fields = ['breed','description','age']

class DogDelete(DeleteView):
    model= Dog
    success_url = '/dogs'