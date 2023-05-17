from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name="customadmin"),
    path('login/', views.admin_login, name="admin_login"),
    path('register/', views.admin_register, name="admin_register"),

] 