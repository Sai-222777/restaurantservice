from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def home_page(request):
    return render(request,"users/home_page.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            messages.success(request,("THERE WAS AN ERROR!"))
            return redirect('login_page')
    else:
        return render(request,"users/login_page.html")

def logout_user(request):
    logout(request)
    messages.success(request,("You were logged out"))
    return redirect('home_page')

def register_page(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # email = request.POST.get('email')
        # # Create user
        # # user = User.objects.create_user(username=username, password=password, email=email)
        # # user.save()
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,("Registered Successfully"))
            return redirect('home_page')
    else:
        form = UserCreationForm()
    return render(request,"users/register_page.html",{'form':form,})


def menu(request):
    return render(request,"users/menu_page.html")

# users/views.py
from django.conf import settings
from django.http import HttpResponse
import pprint

def debug_db(request):
    return HttpResponse(pprint.pformat(settings.DATABASES))
