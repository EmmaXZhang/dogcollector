from django.urls import path
from . import views

# root url: localhose:8000/
urlpatterns = [
    # route, action_function, name of the url/route
    path("",views.home,name="home"),
    path('about/',views.about,name='about'),
    path('cats/',views.cats_index,name='index')
]