import re
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


def validate_letters_and_dashes(value):
    if not re.match(r'^[a-zA-Z]+(?:-[a-zA-Z]+)*$', value):
        raise ValidationError('Only letters and dashes between letters are allowed, with no leading or trailing dashes.')


def validate_no_spaces(value):
    if ' ' in value:
        raise ValidationError("Username cannot contain spaces.")


def validate_phone_number(value):
    regex = r'^(0|\+359)\d{9}$'
    if not value or not bool(re.match(regex, value)):
        raise ValidationError('Invalid phone number format. Phone number should start with 0 or +359 '
                              'and be exactly 10 digits long.')

