from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('log',views.log,name='log'),
    path('alogin',views.alogin,name='alogin'),
    path('addpost',views.addpost,name='addpost'),
    path('showsblogs',views.showsblogs,name='showsblogs'),
    path('editblogs/<int:id>',views.editblogs,name='editblogs'),
    path('new_post',views.new_post,name='new_post'),
    path('editpost/<int:id>',views.editpost,name='editpost'),
    path('deletepost/<int:id>',views.deletepost,name='deletepost'),
    path('signout',views.signout,name='signout'),
    path('ulogin',views.ulogin,name='ulogin'),
    path('user_signout',views.user_signout,name='user_signout'),
    path('details/<int:id>',views.details,name='details'),
]