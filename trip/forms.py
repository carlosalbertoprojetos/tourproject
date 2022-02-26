from django import forms

from .models import Products


class ProductForm(forms.ModelForm):
    fieldsets = [
        ('Identificação', {'fields': [
            ('category', 'name'),
        ]}),
        ('Detalhes', {'fields': [
            ('price', 'available'),
            'description', 
        ]}),
        
        ('Controle', {'fields': [
            'created_at',
            'updated',
        ]}),
        
        ('Situação/Etnia', {'fields': [
            'status',
        ]}),
    ]

    class Meta:
        model = Products
        fields = '__all__'
        exclude = ['user',]
        readonly_fields = ['created_at', 'updated_at']




