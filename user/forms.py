from allauth.account.forms import SignupForm
from basics.utils import sanitize_number
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import ContactMixin, SocialMediaMixin, User


class CustomSignupForm(SignupForm):

    option = forms.CharField(
        label=_('Opção'),
        # choices=OPTION_CHOICES,
        widget=forms.Select
    )

    def clean_password1(self):
        password = self.data.get('password1')
        lpassword = len(password)

        if lpassword < 8 or lpassword > 16:
            raise ValidationError('A senha deve ter de 8 a 16 caracteres')

        if not any(char.isdigit() for char in password):
            raise ValidationError('A senha deve conter pelo menos 1 dígito')

        if not any(char.isalpha() for char in password):
            raise ValidationError('A senha deve conter pelo menos 1 letra')

        return password

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.option = self.cleaned_data.get('option')
        user.save()
        return user


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['document_kind', 'document_number', 'document_image',
                  'postal_code', 'street', 'number', 'complement', 'city', 'state']


class SignupComplementForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'document_kind',
            'document_number',
            'document_image',
            'postal_code',
            'street',
            'number',
            'complement',
            'city',
            'state'
        )

    def clean_document_number(self):
        data = self.cleaned_data['document_number']
        data = sanitize_number(data)
        if User.objects.filter(document_number=data).count():
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

    def get_name(self, data):
        splited = data.split(' ', maxsplit=1)
        if len(splited) > 1:
            return splited
        return data, ''


class PhoneFormSet(forms.Form):

    class Meta:
        model = ContactMixin
        fields = '__all__'

    def clean_cel_phone(self):
        data = self.cleaned_data['cel_phone']
        return sanitize_number(data)

    def save(self, commit=False):
        instance = super().save(commit=commit)
        instance.save()
        return instance


class SocialFormSet(forms.Form):

    class Meta:
        model = SocialMediaMixin
        fields = '__all__'

    def save(self, commit=False):
        instance = super().save(commit=commit)
        instance.save()
        return instance
