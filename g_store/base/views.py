from django.shortcuts import render, redirect
from inventory.models import Product
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, ProfileUpdateForm
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required



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
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out.!"))
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
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
        else:
            form = SignUpForm()
            return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})


@login_required(login_url='login')
def profile(request, pk):
    return render(request, 'profile.html')


@login_required(login_url='login')
def update_profile(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'profile.html')
    else:
        form = ProfileUpdateForm(instance=user)

    return render(request, 'update_profile.html', {'form': form})
