from django.urls import path
from . import views

# root url: localhose:8000/
urlpatterns = [
    # route, action_function, name of the url/route
    path("",views.home,name="home"),
    path('about/',views.about,name='about'),
    path('dogs/',views.dogs_index,name='index'),
    path('dogs/<int:dog_id>',views.dogs_detail,name="detail"),

    # add feeding model
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),

    # add a dog
    path('dogs/create/',views.DogCreate.as_view(),name="dogs_create"),
    #udpate
    path('dogs/<int:pk>/update',views.DogUpdate.as_view(),name='dogs_update'),
    #delete
    path('dogs/<int:pk>/delete',views.DogDelete.as_view(),name='dogs_delete'),
    path('dogs/<int:dog_id>/add_toy/<int:toy_id>/',views.add_toy,name='add_toy'),
    path('dogs/<int:dog_id>/remove_toy/<int:toy_id>/',views.remove_toy,name='remove_toy'),


    path('toys/',views.ToyList.as_view(),name='toys_index'),
    path('toys/<int:pk>/',views.ToyDetail.as_view(),name='toys_detail'),
    path('toys/create/',views.ToyCreate.as_view(),name="toys_create"),
    path('toys/<int:pk>/update',views.ToyUpdate.as_view(),name='toys_update'),
    path('toys/<int:pk>/delete',views.ToyDelete.as_view(),name='toys_delete'),
]