from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from app.models import Product, Variation
from carts.models import Cart, CartItem
from category.models import *
from members.models import *
from django.utils.text import slugify


# Create your views here.
def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        if user and user.is_superadmin:
            auth.login(request, user)
            # messages.success(request, 'Your are now logged in.')
            return redirect("dashboard")
        else:
            messages.error(request, "invalid login credentials")
            return redirect("admin_login")
    return render(request, "myadmin/login.html")


@login_required(login_url="admin_login")
def admin_logout(request):
    auth.admin_logout(request)
    messages.success(request, "you are logged out.")
    return redirect("admin_login")


def dashboard(request):
    return render(request, "myadmin/dashboard.html")


def error404(request):
    return render(request, "myadmin/error404.html")


def products(request):
    products = Product.objects.all()
    return render(request, "myadmin/products.html", {"products": products})


def addproduct(request):
    if request.method == "POST":
        # Process form submission
        product_name = request.POST["product_name"]
        slug = slugify(product_name)
        description = request.POST["description"]
        selling_price = request.POST["selling_price"]
        discounted_price = request.POST["discounted_price"]
        product_detail_ribbon = request.POST["product_detail_ribbon"]
        ribbon = request.POST["ribbon"]
        image1 = request.FILES["image1"]
        image2 = request.FILES["image2"]
        image3 = request.FILES["image3"]
        image4 = request.FILES["image4"]
        image5 = request.FILES["image5"]
        image6 = request.FILES["image6"]
        stock = request.POST["stock"]
        category_id = request.POST["category"]

        category = get_object_or_404(
            Category, id=category_id
        )  # Retrieve the Category instance

        product = Product(
            product_name=product_name,
            slug=slug,
            description=description,
            selling_price=selling_price,
            discounted_price=discounted_price,
            product_detail_ribbon=product_detail_ribbon,
            ribbon=ribbon,
            image1=image1,
            image2=image2,
            image3=image3,
            image4=image4,
            image5=image5,
            image6=image6,
            stock=stock,
            category=category,
        )
        product.save()

        messages.success(request, "Product added successfully.")
        return redirect("addproduct")
    return render(request, "myadmin/addproduct.html")


def variations(request):
    variations = Variation.objects.all()
    context = {
        "variations": variations,
    }
    return render(request, "myadmin/variations.html", context)


def cartitems(request):
    cartitems = CartItem.objects.all()
    context = {
        "cartitems": cartitems,
    }
    return render(request, "myadmin/cartitems.html", context)


def carts(request):
    carts = Cart.objects.all()
    context = {
        "carts": carts,
    }
    return render(request, "myadmin/carts.html", context)


def categories(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, "myadmin/categories.html", context)


def accounts(request):
    accounts = Account.objects.all()
    context = {
        "accounts": accounts,
    }
    return render(request, "myadmin/accounts.html", context)


def addvariation(request):
    return render(request, "myadmin/addvariation.html")


def addcategory(request):
    return render(request, "myadmin/addcategory.html")
