from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.admin_login, name="admin_login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("products", views.products, name="products"),
    path("variations", views.variations, name="variations"),
    path("cartitems", views.cartitems, name="cartitems"),
    path("carts", views.carts, name="carts"),
    path("categories", views.categories, name="categories"),
    path("accounts", views.accounts, name="accounts"),
    path("error404", views.error404, name="error404"),
]
