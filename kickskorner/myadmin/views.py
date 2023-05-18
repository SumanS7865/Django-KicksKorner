from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from app.models import Product


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


def variations(request):
    return render(request, "myadmin/variations.html")


def cartitems(request):
    return render(request, "myadmin/cartitems.html")


def carts(request):
    return render(request, "myadmin/carts.html")


def categories(request):
    return render(request, "myadmin/categories.html")


def accounts(request):
    return render(request, "myadmin/accounts.html")


def addproduct(request):
    return render(request, "myadmin/addproduct.html")


def addvariation(request):
    return render(request, "myadmin/addvariation.html")


def addcategory(request):
    return render(request, "myadmin/addcategory.html")
