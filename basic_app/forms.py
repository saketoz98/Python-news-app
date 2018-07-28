from django import forms
from basic_app.models import Category

class SelectCategory(forms.ModelForm):
    class Meta():
        model = Category
        fields = ['category','country']
        
