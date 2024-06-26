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
    path("sliders", views.sliders, name="sliders"),
    path("staffs", views.staffs, name="staffs"),
    path("accounts", views.accounts, name="accounts"),
    path("orders", views.orders, name="orders"),
    path("error404", views.error404, name="error404"),
    path("addproduct", views.addproduct, name="addproduct"),
    path("addvariation", views.addvariation, name="addvariation"),
    path("addcategory", views.addcategory, name="addcategory"),
    path("invoice", views.invoice, name="invoice"),
    path(
        "delete_product/<int:product_id>/", views.delete_product, name="delete_product"
    ),
    path(
        "delete_category/<int:category_id>/",
        views.delete_category,
        name="delete_category",
    ),
    path(
        "delete_variation/<int:variation_id>/",
        views.delete_variation,
        name="delete_variation",
    ),
]
