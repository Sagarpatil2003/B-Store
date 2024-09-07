from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "published_date", "price", "photo"]
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

# class UserRegistrationForm(UserCreationForm):
#     email =forms.EmailField()
#     class Meta:
#         model = User
#         fields = ('username','email','password1','password2')

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')