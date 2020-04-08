from django.urls import path, include, re_path
from . import views
from django.views.static import serve 
from django.conf import settings



urlpatterns= [

    path('', views.index, name='index'),
    path('sortA/', views.sort_articles_ascending, name='ascending'),
    path('sortD/', views.sort_articles_descending, name='descending'),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]