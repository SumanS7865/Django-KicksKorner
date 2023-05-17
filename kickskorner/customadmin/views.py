from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def dashboard(request):
    return render (request, 'customadmin/dashboard.html')

def admin_login(request):
    return render (request, 'customadmin/login.html')

def admin_register(request):
    return render (request, 'customadmin/register.html')