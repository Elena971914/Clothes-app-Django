from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from clothesDjango.accounts.models import MyUser, Profile
from clothesDjango.catalogue.models import Cloth

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class ProfileEditForm(forms.ModelForm):
    def clean_username(self):
        # Get the cleaned username value
        username = self.cleaned_data.get('username')

        # Check if the username has at least 3 characters and no spaces
        if len(username) < 3 or ' ' in username:
            raise forms.ValidationError("Username must be at least 3 characters long and cannot contain spaces.")

        return username

    class Meta:
        model = UserModel
        fields = ['email', 'username', 'first_name', 'last_name',
                  'date_of_birth', 'phone_number', 'address', 'city', 'postal_code']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'})
        }


