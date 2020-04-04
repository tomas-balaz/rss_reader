from django.urls import path, include
from . import views


urlpatterns= [

    path('', views.index, name='index'),
    path('sortA/', views.sort_a, name='ascending'),
    path('sortD/', views.sort_d, name='descending')

]