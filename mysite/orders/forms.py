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

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for field in self.fields:
                self.fields[field].widget.attrs.update({
                    "class": (
                        "w-full rounded-md border border-gray-300 "
                        "px-3 py-2 "
                        "focus:outline-none "
                        "focus:ring-2 focus:ring-orange-500 "
                        "focus:border-orange-500"
                    )
                })