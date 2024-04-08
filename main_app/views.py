from django.shortcuts import render

# should come from database
dogs = [
  {'name': 'Lolo', 'breed': 'Corgi', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'Pomeranian', 'description': 'gentle and loving', 'age': 2},
]


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def dogs_index(request):
    return render(request,'dogs/index.html',{
        'dogs':dogs
    })