from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import PurchaseForm



# Create your views here.
def show_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product:
        return render(request, 'product.html', {'product': product})      
    return redirect('home')


def buy_product(request, pk):
    product = get_object_or_404(Product, id=pk)

    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.product = product
            purchase.user = request.user
            purchase.total_amount = product.price * purchase.quantity
            purchase.save()
            product.count -= purchase.quantity
            product.save()
            return redirect('billing', purchase_id=purchase.id)
    else:
        form = PurchaseForm(initial={'product': product})

    context = {'product': product, 'form': form}
    return render(request, 'buy_product.html', context)