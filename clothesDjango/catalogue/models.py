from django.db import models
from django.db.models import Model

from clothesDjango.catalogue.validators import image_size_validator


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
    photo_1 = models.ImageField(validators=[image_size_validator], null=True, blank=True)
    photo_2 = models.ImageField(validators=[image_size_validator], null=True, blank=True)
    photo_3 = models.ImageField(validators=[image_size_validator], null=True, blank=True)
    photo_4 = models.ImageField(validators=[image_size_validator], null=True, blank=True)
    photo_5 = models.ImageField(validators=[image_size_validator], null=True, blank=True)
    type = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    name = models.CharField(
        max_length=100
    )
    price = models.IntegerField(
    )
    color = models.CharField(
        max_length=20
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

    def __str__(self):
        return f'{self.name}'
