from django import forms

from clothesDjango.catalogue.models import Cloth
from clothesDjango.orders.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address', 'is_personal_address', 'payment_method', 'phone', 'comment']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cloth'].queryset = Cloth.objects.all()  # Assuming Cloth is your Cloth model

        if user.address:
            self.initial['delivery_address'] = user.address
        if user.phone_number:
            self.initial['phone_number'] = user.phone_number

    def clean(self):
        cleaned_data = super().clean()
        is_personal_address = cleaned_data.get('is_personal_address')
        delivery_address = cleaned_data.get('delivery_address')

        if not is_personal_address and not delivery_address:
            raise forms.ValidationError("Please provide a delivery address.")

        return cleaned_data
