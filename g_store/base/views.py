from django.shortcuts import render, redirect
from inventory.models import Product
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def index(request):
    products = Product.objects.all().order_by("-id")
    context = {'products': products}
    return render(request, 'index.html', context)


def login_user(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			return redirect('home')
	else:
		return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    return render(request, 'register.html')


def profile(request, pk):
    return render(request, 'profile.html')