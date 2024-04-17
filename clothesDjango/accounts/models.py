
from django.contrib.auth import models as auth_models, get_user_model
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.utils import timezone

from clothesDjango.accounts.validators import validate_before_today, validate_age, validate_letters_and_dashes, \
    validate_phone_number, validate_no_spaces


class MyUser(auth_models.AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            MinLengthValidator(4, message="Username must be at least 4 characters long."),
            validate_no_spaces
        ]
    )
    email = models.EmailField(
        unique=True
    )
    first_name = models.CharField(
        validators=[validate_letters_and_dashes],
        max_length=30,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        validators=[validate_letters_and_dashes],
        max_length=30,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        validators=[validate_phone_number],
        max_length=10,
        null=True,
        blank=True
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        null=True)
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True)
    postal_code = models.CharField(
        max_length=100,
        blank=True,
        null=True)
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='myuser_permissions',
        help_text='Specific permissions for this user.',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='myuser_groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class AdminUser(MyUser):
    class Meta:
        permissions = [
            ("can_add_clothes", "Can add clothes"),
        ]

    def __str__(self):
        return f"Admin: {self.username}"


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)

