from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}))
    address = forms.CharField(label="Address", max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))
    street = forms.CharField(label="Street", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Street'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    phone = forms.CharField(label="Phone", max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    quantity = forms.IntegerField(label="Quantity", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'1'}))
 
    class Meta:
        model = Purchase
        fields = ['product', 'quantity', 'name', 'address', 'street', 'email', 'phone']
        widgets = {'product': forms.HiddenInput(),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['min'] = 1  
