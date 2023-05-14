from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# # Signup views
# def signuppage(request):
#     if request.method == 'POST':
#         uname = request.POST['username']
#         email = request.POST['email']
#         pass1 = request.POST['password1']
#         pass2 = request.POST['password2']

#         if pass1!=pass2:
#             return HttpResponse ("Password did not match")
        
#         else:
#             myuser = User.objects.create_user(uname, email, pass1)
#             myuser.save()
#             return redirect ('loginform')
        
#     return render (request, 'register.html')


# def loginpage(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         pass1=request.POST['password']
#         user = authenticate(request,username=username,password=pass1)

#         if user is not None:
#             login(request,user)
#             return redirect('index')
#         else:
#             return HttpResponse("Username or Password is invalid !")
        
#     return render(request,'login.html')

# def LogoutPage(request):
#     logout(request)
#     return redirect('loginform')


def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return