from django.db import models

from clothesDjango.accounts.validators import validate_before_today, validate_age
from clothesDjango.catalogue.models import Cloth


class User(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    birth_date = models.DateField(
        validators=[validate_before_today, validate_age]
    )
    agreed_to_terms = models.BooleanField(
        null=False,
        blank=False,
    )
    orders = models.ManyToManyField(
        Cloth,
        through='Ordered'
    )


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Ordered(models.Model):
    purchases = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    purchased = models.ForeignKey(Cloth, on_delete=models.SET_NULL, null=True)
    date_of_purchase = models.DateField(auto_now=True)
