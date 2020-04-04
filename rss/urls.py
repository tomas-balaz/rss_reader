from django.urls import path, include
from . import views


urlpatterns= [

    path('', views.index, name='index'),
    path('sortA/', views.sort_articles_ascending, name='ascending'),
    path('sortD/', views.sort_articles_descending, name='descending')

]