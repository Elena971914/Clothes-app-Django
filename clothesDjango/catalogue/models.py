from django.db import models
from django.db.models import Model


class Cloth(models.Model):
    T_SHIRT = 'tshirt'
    JEANS = 'jeans'
    SKIRT = 'skirt'
    BLOUSE = 'blouse'
    JACKET = 'jacket'
    TROUSERS = 'trousers'
    SOCKS = 'socks'
    TOP = 'top'
    UNDERWEAR = 'underwear'

    CATEGORY_CHOICES = [
        (T_SHIRT, 'tshirt'),
        (JEANS, 'jeans'),
        (SKIRT, 'skirt'),
        (BLOUSE, 'blouse'),
        (JACKET, 'jacket'),
        (TROUSERS, 'trousers'),
        (SOCKS, 'socks'),
        (TOP, 'top'),
        (UNDERWEAR, 'underwear'),
    ]
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
    size = models.CharField(
        max_length=10
    )

