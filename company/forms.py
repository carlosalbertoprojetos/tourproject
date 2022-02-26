from company.utils import sanitize_number
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Company


class Signup2Form(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'responsible',
            'company_name',
            'document_number',
            'street',
            'number',
            'complement',
            'postal_code',
            'city',
            'state'
        )

    def __init__(self, *args, **kwargs):
        super(Signup2Form, self).__init__(*args, **kwargs)
        self.fields['document_number'].widget.attrs.update(
            {'class': 'mask-cnpj'})
        self.fields['state'].widget.attrs.update({'class': 'mask-state'})
        self.fields['postal_code'].widget.attrs.update({'class': 'mask-cep'})
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = sanitize_number(email)
        queryset = Company.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError('Já existe um usuário cadastrado com esse email.')
        return email

    def clean_document_number(self):
        document_number = self.cleaned_data['document_number']
        document_number = sanitize_number(document_number)
        queryset = Company.objects.filter(
            document_number=document_number).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Documento já cadastrado.')
        return document_number

    def clean_postal_code(self):
        data = self.cleaned_data['postal_code']
        return sanitize_number(data)

    def save(self, commit=False):
        instance = super().save(commit=commit)
        instance.save()
        return instance


class CompanyEditForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document_number'].widget.attrs.update(
            {'class': 'mask-cnpj'})
        self.fields['state'].widget.attrs.update({'class': 'mask-state'})
        self.fields['postal_code'].widget.attrs.update({'class': 'mask-cep'})
        
    def clean_email(self):
        email = self.cleaned_data.get['email']
        email = sanitize_number(email)
        queryset = Company.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError('Já existe um usuário cadastrado com esse email.')
        return email
   
    def clean_document_number(self):
        document_number = self.cleaned_data['document_number']
        document_number = sanitize_number(document_number)
        queryset = Company.objects.filter(
            document_number=document_number).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Documento já cadastrado.')
        return document_number
    
    def clean_postal_code(self):
        data = self.cleaned_data['postal_code']
        return sanitize_number(data)

    def save(self, commit=False):
        instance = super().save(commit=commit)
        instance.save()
        return instance