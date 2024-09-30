# forms.py
from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'page', 'price'] 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book', 'review']  