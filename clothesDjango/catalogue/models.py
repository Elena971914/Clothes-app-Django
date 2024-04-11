from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Model

from clothesDjango.catalogue.validators import image_size_validator

UserModel = get_user_model()


class Cloth(models.Model):
    class Meta:
        ordering = ['price']
        verbose_name_plural = 'Clothes'

    CATEGORY_CHOICES = [
        ('DRESS', 'dress'),
        ('T_SHIRT', 't-shirt'),
        ('JEANS', 'jeans'),
        ('SKIRT', 'skirt'),
        ('BLOUSE', 'blouse'),
        ('JACKET', 'jacket'),
        ('TROUSERS', 'trousers'),
        ('SOCKS', 'socks'),
        ('TOP', 'top'),
        ('UNDERWEAR', 'underwear'),
    ]

    type = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    price = models.IntegerField(
    )
    color = models.CharField(
        max_length=20
    )
    material = models.CharField(
        max_length=20,
        null=True
    )
    size = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    stocked_S = models.PositiveIntegerField(
        default=0
    )
    stocked_M = models.PositiveIntegerField(
        default=0
    )
    stocked_L = models.PositiveIntegerField(
        default=0
    )

    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to='clothes_images',
        validators=[image_size_validator]
    )

    def __str__(self):
        return f'{self.name}'

