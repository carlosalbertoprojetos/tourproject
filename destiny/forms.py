from django import forms

from .models import Destiny


class DestinyForm(forms.ModelForm):

    class Meta:
        model = Destiny
        fields = ("name", "state", "city", "is_active")
        widgets = {
            "name": forms.Select(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "col-3 col-lg-1 form-control"}),
        }
