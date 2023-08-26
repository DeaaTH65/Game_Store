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


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)