from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout


from .models import Category, Brand, Product, Cart

# Create your views here.
def home(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'home.html')

def shop(request):
    products = Product.objects.all()  # Example query to fetch all products
    # return HttpResponse(products)
    context = {
        'products': products,
    }
    return render(request, 'shop.html', context)

def shop_details(id):
    product = Product.objects.get(id=id)
    # return HttpResponse(product)
    return render('shop_details.html' , {'product':product})

def checkout(request):
    return render(request,'checkout.html')

def shopping_cart(request):
    products = Product.objects.all() # Example queryset to fetch all products
      # return HttpResponse(products)
    context = {
        'products': products,
    }
    return render(request, 'shopping_cart.html', context)

    
# Create your views here.
def about(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'about.html')

def blog_details(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'blog_details.html')


def contact(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'contact.html')

def footer(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'footer.html')

def header(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'header.html')

def blog(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'blog.html')
