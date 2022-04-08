from django import forms

from .models import CategoryPax


class CategoryPaxForm(forms.ModelForm):
    
    class Meta:
        model = CategoryPax
        fields = '__all__'
