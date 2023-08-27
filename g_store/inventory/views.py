from django.shortcuts import render, redirect, get_object_or_404
from .models import Product




# Create your views here.
def show_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product:
        return render(request, 'product.html', {'product': product})      
    return redirect('home')


