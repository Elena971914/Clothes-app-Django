from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from clothesDjango.accounts.validators import validate_before_today, validate_age, validate_letters_and_dashes
from clothesDjango.catalogue.models import Cloth


class MyUser(auth_models.AbstractUser):
    email = models.EmailField(
        unique=True
    )
    first_name = models.CharField(
        validators=[MinLengthValidator(30), validate_letters_and_dashes],
        max_length=30
    )
    last_name = models.CharField(
        validators=[MinLengthValidator(30), validate_letters_and_dashes],
        max_length=30
    )
    date_of_birth = models.DateField(
        validators=[validate_age],
        null=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='myuser_permissions',  # Unique related name
        help_text='Specific permissions for this user.',
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='myuser_groups',  # Unique related name
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )


class AdminUser(MyUser):
    pass


class ClientUser(MyUser):
    pass


# class Order(models.Model):
#     to_cloth = models.ForeignKey(
#         Cloth,
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True
#         )
#     date_of_purchase = models.DateField(
#         auto_now=True,
#         null=True,
#         blank=True
#     )
#
#
# class Like(models.Model):
#     to_cloth = models.ForeignKey(
#         Cloth,
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True
#     )


class Cart(models.Model):
    to_cloth = models.ForeignKey(
        Cloth,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
