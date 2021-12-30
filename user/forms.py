from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from user.models import User


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


# class AgentSignupForm(SignupForm):
    
#     option = forms.CharField(max_length=1)

#     def clean_password1(self):
#         password = self.data.get('password1')
#         lpassword = len(password)

#         if lpassword < 8 or lpassword > 16:
#             raise ValidationError('A senha deve ter de 8 a 16 caracteres')

#         if not any(char.isdigit() for char in password):
#             raise ValidationError('A senha deve conter pelo menos 1 dígito')

#         if not any(char.isalpha() for char in password):
#             raise ValidationError('A senha deve conter pelo menos 1 letra')

#         return password

#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         user.option = '4'
#         user.save()
#         return user

# class AgentSignupForm(forms.ModelForm):
    
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email',]

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_2 = cleaned_data.get("password_2")
#         if password is not None and password != password_2:
#             self.add_error("password_2", "As senhas precisam ser iguais.")
#         return cleaned_data

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user