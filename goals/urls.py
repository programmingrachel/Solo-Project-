from django.urls import path
from . import views

# from django.urls import path, re_path
# from .views import ViewsToBeImported

# app_name = AppName

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('homepage',views.home),
    path('setgoal',views.setgoal),
    path('editgoal',views.editgoal),
    path('viewgoals',views.goals),
    path('editprofile',views.editprofile),
    path('logout',views.logout)
]