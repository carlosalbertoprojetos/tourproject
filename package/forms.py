from django import forms

from .models import Data_Package_One, Child_Package_One
# ,Data_Customer_Package


class Data_Package_OneForm(forms.ModelForm):


    class Meta:
        model = Data_Package_One
        # fields = ['date_arrive', 'date_departure', 'num_adults', 'num_child']
        fields = '__all__'
        exclude = ['destiny']
        widgets = {
            'date_arrive':forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class':'my-1',
                    'type':'date',
                    'required': 'true'
                    },
                ),
            'date_departure':forms.DateInput(
                attrs={
                    'class':'my-1',
                    'type':'date',
                    'required': 'true'
                    },
                ),            
            'num_adults':forms.NumberInput(
                attrs={
                    'class':'my-1',
                    'type':'number',
                    'required': 'true'
                    },
                ),                        
            'num_child':forms.NumberInput(
                attrs={
                    'class':'my-1',
                    'type':'number',
                    'required': 'true'
                    },
                ),
        }

class Child_Package_OneForm(forms.ModelForm):

    class Meta:
        model = Child_Package_One
        fields = ('children_age',)
        labels = {"Data_package_one":''}
        widgets = {
            'children_age':forms.NumberInput(
                attrs={
                    'class':'form-control mx-1 text-center',
                    'size': '2',
                    'type':'text',
                    # 'required': 'true' - não salva
                    },
                ),
            }

# class Data_Customer_PackageForm(forms.ModelForm):

#     class Meta:
#         model = Data_Customer_Package
#         fields = ('name', 'email', 'phonenumber', 'city', 'description')
#         widgets = {
#             'name':forms.TextInput(
#                 attrs={
#                     'class':'col-md-12 form-control mx-1 text-center',
#                     'type':'text',
#                     'required': 'true'
#                     },
#                 ),
#             'email':forms.TextInput(
#                 attrs={
#                     'class':'col-md-6 form-control mx-1 text-center',
#                     'type':'email',
#                     'required': 'true'
#                     },
#                 ),
#             'phonenumber':forms.TextInput(
#                 attrs={
#                     'class':'col-md-6 form-control mx-1 text-center',
#                     'type':'text',
#                     'required': 'true',
#                     'data-inputmask-mask':'"(9-)AAAAA-9999"',
#                     },
#                 ),
#             'city':forms.TextInput(
#                 attrs={
#                     'class':'col-md-12 form-control mx-1 text-center',
#                     'type':'text',
#                     'required': 'true'
#                     },
#                 ),
#             'description':forms.TextInput(
#                 attrs={
#                     'class':'col-md-12 form-control mx-1 text-center',
#                     'type':'text',
#                     'required': 'true'
#                     },
#                 ),
#             }