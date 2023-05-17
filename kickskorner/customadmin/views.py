from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.


def dashboard(request):
    return render(request, "customadmin/dashboard.html")


def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        if user and user.is_superadmin:
            auth.login(request, user)
            # messages.success(request, 'Your are now logged in.')
            return redirect("customadmin")
        else:
            messages.error(request, "invalid login credentials")
            return redirect("admin_login")

    return render(request, "customadmin/login.html")


@login_required(login_url="admin_login")
def admin_logout(request):
    auth.admin_logout(request)
    messages.success(request, "you are logged out.")
    return redirect("admin_login")


def admin_register(request):
    return render(request, "customadmin/register.html")


def error404(request):
    return render(request, "customadmin/error404.html")


def products(request):
    return render(request, "customadmin/products.html")
