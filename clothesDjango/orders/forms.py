from django import forms
from .models import Order
from ..accounts.validators import validate_letters_and_dashes, validate_phone_number


class OrderForm(forms.Form):
    PAYMENT_METHOD_CHOICES = (
        ('CARD', 'Card payment'),
        ('CASH', 'Cash on delivery'),
    )
    first_name = forms.CharField(max_length=30, validators=[validate_letters_and_dashes], error_messages={'invalid': 'Please enter a valid phone number.'}, widget=forms.TextInput(attrs={'placeholder': 'First name of receiver'}))
    last_name = forms.CharField(max_length=30, validators=[validate_letters_and_dashes], widget=forms.TextInput(attrs={'placeholder': 'Last name of receiver'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(max_length=10, validators=[validate_phone_number],widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    delivery_address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Delivery address (street, number, building, entrance, etc.)'}))
    city = forms.CharField(max_length=100, validators=[validate_letters_and_dashes], widget=forms.TextInput(attrs={'placeholder': 'City'}))
    postal_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Postal code'}))
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, initial='CASH')
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Additional comments (optional)'}), required=False)
    is_personal_address = forms.BooleanField(initial=True, required=False)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args)
        self.user = user

        if user.first_name:
            self.initial['first_name'] = user.first_name
        if user.last_name:
            self.initial['last_name'] = user.last_name
        if user.email:
            self.initial['email'] = user.email
        if user.address:
            self.initial['delivery_address'] = user.address
        if user.phone_number:
            self.initial['phone'] = user.phone_number
        if user.city:
            self.initial['city'] = user.city
        if user.postal_code:
            self.initial['postal_code'] = user.postal_code

    def clean(self):
        cleaned_data = super().clean()
        is_personal_address = cleaned_data.get('is_personal_address')
        delivery_address = cleaned_data.get('delivery_address')

        if not is_personal_address and not delivery_address:
            raise forms.ValidationError("Please provide a delivery address.")

        return cleaned_data

    def save(self):
        order = Order(
            user=self.user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data['phone'],
            delivery_address=self.cleaned_data['delivery_address'],
            city=self.cleaned_data['city'],
            postal_code=self.cleaned_data['postal_code'],
            payment_method=self.cleaned_data['payment_method'],
            comment=self.cleaned_data['comment'],
            is_personal_address=self.cleaned_data['is_personal_address'],
        )
        order.save()
        return order
