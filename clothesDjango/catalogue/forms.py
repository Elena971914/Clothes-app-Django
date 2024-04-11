from django import forms

from clothesDjango.catalogue.models import Cloth
from clothesDjango.catalogue.validators import validate_letters_and_spaces


class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by name, color or type...'
            }
        ),
        validators=[validate_letters_and_spaces]
    )


class AddClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        exclude = ('size',)

