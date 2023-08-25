from django.shortcuts import render
from inventory.models import Product



# Create your views here.
def index(request):
    products = Product.objects.all().order_by("-id")
    context = {'products': products}
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def profile(request, pk):
    return render(request, 'profile.html')