from django.urls import path

from . import views


app_name = 'frontendaClub'
urlpatterns = [
    path('', views.homeView, name='home'),
    path('post', views.newPostView, name='newPost'),
    path('about', views.aboutView, name='about'),
]
