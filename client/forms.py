from django import forms


from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'cpf',
            'street',
            'number',
            'complement',
            'postal_code',
            'state',
            'city',
            'email',
            'phoneNumber',
            'is_active',
        ]

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.attrs.get('class'):
                field.widget.attrs['class'] += ' form-control form-control-sm'
            else:
                field.widget.attrs['class'] = 'form-control form-control-sm'

# Abaixo está como você pode usar esse formulário na sua template
