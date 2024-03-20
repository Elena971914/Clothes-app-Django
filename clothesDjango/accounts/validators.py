from datetime import date

from django.core.exceptions import ValidationError


def validate_before_today(value):
    if date.today() < value:
        raise ValidationError(f'{value} is in the future')


def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 14:
        raise ValidationError('Users must be at least 14 years old.')
