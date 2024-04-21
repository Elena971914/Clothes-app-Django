from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Model
from django.utils import timezone

from clothesDjango.catalogue.validators import image_size_validator, validate_letters_and_spaces

UserModel = get_user_model()


class Cloth(models.Model):
    class Meta:
        ordering = ['-creation_date']
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
        ('SWEATSHIRT', 'sweatshirt'),
        ('TRACK_SUIT', 'track-suit')
    ]

    type = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=100,
        validators=[validate_letters_and_spaces],
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True,
        validators=[validate_letters_and_spaces]
    )
    price = models.IntegerField(
        null=False,
        blank=False
    )
    color = models.CharField(
        max_length=20,
        validators=[validate_letters_and_spaces],
        null=False,
        blank=False
    )
    material = models.CharField(
        max_length=50,
        validators=[validate_letters_and_spaces],
        default='mixture of bio materials',
        null=False,
        blank=False,
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
        max_length=300,
        null=True,
        blank=True,
        upload_to='clothes_images',
        validators=[image_size_validator]
    )
    photo_2 = models.ImageField(
        max_length=300,
        null=True,
        blank=True,
        upload_to='clothes_images',
        validators=[image_size_validator]
    )
    photo_3 = models.ImageField(
        max_length=300,
        null=True,
        blank=True,
        upload_to='clothes_images',
        validators=[image_size_validator]
    )
    photo_4 = models.ImageField(
        max_length=300,
        null=True,
        blank=True,
        upload_to='clothes_images',
        validators=[image_size_validator]
    )
    photo_5 = models.ImageField(
        max_length=300,
        null=True,
        blank=True,
        upload_to='clothes_images',
        validators=[image_size_validator]
    )
    photo_6 = models.ImageField(
        max_length=300,
        null=True,
        blank=True,
        upload_to='clothes_images',
        validators=[image_size_validator]
    )
    creation_date = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        return f'{self.name}'

