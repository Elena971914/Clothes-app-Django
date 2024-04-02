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
    class Meta:
        model = MyUser
        fields = ['email', 'username', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'address']


