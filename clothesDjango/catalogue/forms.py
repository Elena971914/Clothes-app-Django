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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color'].widget = forms.TextInput(attrs={'placeholder': 'Write all colors separated by space'})
        self.fields['material'].widget = forms.TextInput(attrs={'placeholder': 'Write all contained materials separated by space'})


class UpdateClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = ('stocked_S', 'stocked_M', 'stocked_L')

