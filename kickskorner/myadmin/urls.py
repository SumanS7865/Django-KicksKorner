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
    path("addproduct", views.addproduct, name="addproduct"),
    path("addvariation", views.addvariation, name="addvariation"),
    path("addcategory", views.addcategory, name="addcategory"),
    path("invoice", views.invoice, name="invoice"),
    path(
        "delete_product/<int:product_id>/", views.delete_product, name="delete_product"
    ),
]
