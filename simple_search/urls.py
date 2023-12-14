from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('imageSearch', views.imageSearch),
    path('advanceSearch', views.advanceSearch),
    path('searching', views.searching, name='searching'),
    path('simplesearch', views.simplesearch, name='simplesearch'),
]