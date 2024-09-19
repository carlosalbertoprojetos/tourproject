from destiny.models import Destiny
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from .models import (
    Activity,
    ActivityPrice,
    CategoryPax,
    Trip,
    TripCategory,
    ActivityCatPax,
)


class TripCategoryForm(forms.ModelForm):

    class Meta:
        model = TripCategory
        fields = "__all__"


class TripForm(forms.ModelForm):
    destiny = forms.ModelChoiceField(queryset=Destiny.objects.all(), label="Destino", widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model = Trip
        fields = "__all__"
        exclude = ("slug",)
        widgets = {
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "trip_description": forms.Textarea(attrs={"class": "form-control"}),
            "short_description": forms.Textarea(attrs={"class": "form-control"}),
            "politic": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "tour_notes": forms.Textarea(attrs={"class": "form-control"}),
            "featured_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        self.fields["trip_duration"].widget.attrs.update({"class": "mask-hora"})
        self.fields["travel_time"].widget.attrs.update({"class": "mask-hora"})
        self.fields["travel_time_untoplace"].widget.attrs.update({"class": "mask-hora"})
        self.fields["commission"].widget.attrs.update({"class": "mask-perc"})


class CategoryPaxForm(forms.ModelForm):
    class Meta:
        model = CategoryPax
        fields = "__all__"

        widgets = {
            "t_adult": forms.CheckboxInput(attrs={"class": ""}),
            "t_child": forms.CheckboxInput(attrs={"class": ""}),
            "t_guest": forms.CheckboxInput(attrs={"class": ""}),
            "age_min": forms.NumberInput(
                attrs={"class": "form-inline col-md-2 text-center"}
            ),
            "age_max": forms.NumberInput(
                attrs={"class": "form-inline col-md-2 text-center"}
            ),
        }


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activity
        fields = "__all__"
        widgets = {
            "trip": forms.Select(attrs={"class": "form-select"}),
            # "name": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            # "catpax": forms.CheckboxSelectMultiple(attrs={"class": "d-flex gap-2"}),
            # "min_amount_pax": forms.NumberInput(attrs={"class": "form-control"}),
            "occ_scale": forms.Select(
                choices=Activity.SCALE_CHOICE, attrs={"class": "form-select"}
            ),
            # "tariff_group": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            # "customer_option": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            # "night_walk": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields["catpax"].widget = CheckboxSelectMultiple()
        self.fields["catpax"].queryset = CategoryPax.objects.all()
        self.fields["catpax"].label_suffix = ""  # Remove the default colon
        # self.fields["catpax"].widget.attrs.update({"class": "d-flex gap-2"})
        self.fields["catpax"].label_tag = (
            lambda: f'<label for="{self["catpax"].id_for_label}" class="d-flex gap-2">Your Label Text</label>'
        )


class ActivityPriceForm(forms.ModelForm):

    class Meta:
        model = ActivityPrice
        fields = [
            "activity",
            "catpax",
            "price",
        ]
        widgets = {
            "activity": forms.TextInput({"readonly": "readonly", "type": "hidden"}),
            "catpax": forms.TextInput({"readonly": "readonly", "type": "hidden"}),
            "price": forms.NumberInput(
                attrs={"class": "text-center", "style": "border: 0; padding: 0 5px;"}
            ),
        }
        labels = {"price": ""}


class CHD_ActivityForm(forms.ModelForm):

    class Meta:
        model = ActivityCatPax
        fields = "__all__"
