from basics.utils import sanitize_number
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

from .models import Company


class Signup2Form(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'company_name',
            'document_number',
            'document_image',
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

    def clean_document_number(self):
        data = self.cleaned_data['document_number']
        data = sanitize_number(data)
        if Company.objects.filter(document_number=data).count():
            raise ValidationError(
                'Já existe um usuário cadastrado com esse documento.')
        return data

    def clean_postal_code(self):
        data = self.cleaned_data['postal_code']
        return sanitize_number(data)

    def save(self, commit=False):
        instance = super().save(commit=commit)
        instance.save()
        return instance


class EditCompanyForm(forms.ModelForm):

    document_image = forms.ImageField(
        widget=ClearableFileInput
    )

    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document_number'].widget.attrs.update(
            {'class': 'mask-cnpj'})
        self.fields['state'].widget.attrs.update({'class': 'mask-state'})
        self.fields['postal_code'].widget.attrs.update({'class': 'mask-cep'})
