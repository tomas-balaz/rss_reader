from django.urls import path, include
from . import views


urlpatterns= [

    path('', views.index, name='index'),
    path('/asc', views.sort_asc, name='sort-asc')

]