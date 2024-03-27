import re

from django.core.exceptions import ValidationError


def image_size_validator(image_object):
    if image_object.size > 10485760:
        raise ValidationError('The maximum file size that can be uploaded is 10MB')


def validate_letters_and_spaces(value):
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValidationError('Only letters and spaces are allowed.')