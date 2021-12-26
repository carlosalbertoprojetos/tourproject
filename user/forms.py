from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomSignupForm(SignupForm):

    OPTION_CHOICES = [
        ('1', _('Agência')),
        ('2', _('Cliente')),
        ('3', _('Parceiro')),
    ]

    option = forms.ChoiceField(
        label=_('Opção'),
        choices=OPTION_CHOICES,
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
