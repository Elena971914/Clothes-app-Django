from django import forms

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
