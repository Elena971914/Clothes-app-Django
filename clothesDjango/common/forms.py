from django import forms

from clothesDjango.common.models import Testimonial


class NewsletterForm(forms.Form):
    email = forms.EmailField()


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        labels = {'text': 'Tell us your opinion. It matters!',
                  'author': 'Your name',
                  'phone': 'Telephone number for contact (Just in case)',
                  'email': 'Your email'
                  }