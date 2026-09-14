from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']
        labels = {
            "full_name": "Nombre completo",
            "phone": "Teléfono",
            "line1": "Dirección 1",
            "line2": "Dirección 2",
            "city": "Ciudad",
            "region": "Región",
            "postal_code": "Código postal",
            "province": "Provincia",
        }