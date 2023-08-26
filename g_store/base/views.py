from django.shortcuts import render, redirect
from inventory.models import Product
from django.contrib.auth import logout



# Create your views here.
def index(request):
    products = Product.objects.all().order_by("-id")
    context = {'products': products}
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    return render(request, 'register.html')


def profile(request, pk):
    return render(request, 'profile.html')