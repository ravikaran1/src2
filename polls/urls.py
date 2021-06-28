from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('loginn', views.loginn, name='loginn'),
    path('logout', views.logout, name='logout'),
    path('addpoll', views.addpoll, name='addpoll'),
    path('profile', views.profile, name='profile'),
    path('editprof', views.editprof, name='editprof'),
    path('yourpolls', views.yourpolls, name='yourpolls'),
    path('delet/<int:myid>', views.delet, name='delet'),


]
