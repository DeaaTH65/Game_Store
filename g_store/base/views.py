from django.shortcuts import render, redirect
from inventory.models import Product
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm



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


def register_user(request):
	form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data['email']
			password = form.cleaned_data['password1']
			user = authenticate(email=email, password=password)
			login(request, user)
			return redirect('home')
		else:
			form = SignUpForm()
			return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def profile(request, pk):
    return render(request, 'profile.html')