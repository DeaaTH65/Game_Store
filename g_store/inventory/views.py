from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Purchase
from .forms import PurchaseForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def show_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product:
        return render(request, 'product.html', {'product': product})      
    return redirect('home')


@login_required(login_url='login')
def buy_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    user = request.user

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
        form = PurchaseForm(initial={'product': product}, instance=user)

    context = {'product': product, 'form': form}
    return render(request, 'buy_product.html', context)


@login_required(login_url='login')
def billing(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id)
    return render(request, 'billing.html', {'purchase': purchase})


def search(request):
	if request.method == "POST":
		# Grab the form field input
		search = request.POST['search']
		# Search the database
		searched = Product.objects.filter(name__contains = search)

		return render(request, 'search.html', {'search':search, 'searched':searched})
	else:
		return render(request, 'search.html')