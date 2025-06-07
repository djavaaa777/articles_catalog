from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article,Review



class CustomerRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True,label='Email')
    class Meta:
        model=User
        fields=['email','username','password1','password2']

class ArticleForm(forms.ModelForm):
        class Meta:
            model=Article
            fields=['title','preview','content','date']
            widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            }

class ReviewForm(forms.ModelForm):
        class Meta:
            model=Review
            fields=['content']
            widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Your thoughts...', 'rows': 4}),
            }
