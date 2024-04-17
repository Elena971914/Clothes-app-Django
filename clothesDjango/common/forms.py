from django import forms

from clothesDjango.common.models import Testimonial


class NewsletterForm(forms.Form):
    email = forms.EmailField()


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        exclude = ('user',)
        labels = {'text': 'Tell us your opinion. It matters!',}