from django.shortcuts import render, redirect
from .models import Product, Maincat, Subcat
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from django.http import HttpResponse


# Create your views here.

def maincategory(request, dummy):
        # catching the items according to category
        category = Maincat.objects.get(name=dummy)
        products = Product.objects.filter(maincat__name =category)
        return render(request, 'maincat.html', {'products':products,'category':category})
        

def subcategory(request,dummy):
     # grabbing category from url
        # catching the items according to category
        category = Subcat.objects.get(name=dummy)
        products = Product.objects.filter(subcat=category)
        return render(request,'subcat.html',{'products':products,'category':category})
    
def mainsubcategory(request,dummy,parent):
    maincat = Maincat.objects.get(name=parent)
    subcat = Subcat.objects.get(name=dummy)
    products = Product.objects.filter(subcat=subcat,maincat=maincat)
    return render(request,'mainsub.html',{'products':products,'subcat':subcat,'maincat':maincat})
    

def index(request):
    products = Product.objects.all()[:8]
    products1 = Product.objects.all()[8:16]
    return render(request, 'index.html',{'products':products,'product1s':products1})    


def shop(request):
     products = Product.objects.all()
     return render(request, 'shop.html',{'products':products,'maincats':Maincat})

def contact(request):
    return render(request, 'contact.html')


def login_user(request):
     if request.method == 'POST':
       username=request.POST['username']
       password= request.POST['password']
       user = authenticate(request, username = username, password = password)
       if user is not None:
           login(request, user)
           messages.success(request, ("You have been logged in!"))
           return redirect('home')
       else:
           messages.success(request, ("There was a error!, please try again"))
           return redirect('login')
     else:
      return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out!"))
    return redirect('home')


def product(request,pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()[:4]
    return render(request, 'product.html',{'product':product,'products':products})


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, ("You have registered successfully welcome!"))
            return redirect('home')
        else:
            messages.success(request, ("OOps! There was a problem in registering, Please try again"))
            return redirect('register')
    else:
            return render(request, 'register.html',{'form':form})
