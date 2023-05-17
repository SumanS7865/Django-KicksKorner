from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.admin_login, name="admin_login"),
    path("dashboard", views.dashboard, name="customadmin"),
    path("error404/", views.error404, name="error404"),
    path("logout/", views.admin_logout, name="admin_logout"),
    path("products/", views.products, name="products"),
]
