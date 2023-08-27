from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'password1', 'password2',)
        

class ProfileUpdateForm(forms.ModelForm):
    picture = forms.ImageField(label="Profile Picture")
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}))
    phone = forms.CharField(label="Phone", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
    social = forms.CharField(label="Social", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Social Link'}))
 
    class Meta:
        model = CustomUser
        fields = ['name', 'phone', 'social', 'picture']
