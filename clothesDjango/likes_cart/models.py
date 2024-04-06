from django.contrib.auth import get_user_model
from django.db import models

from clothesDjango.catalogue.models import Cloth

UserModel = get_user_model()


class Likes(models.Model):
    cloth = models.ForeignKey(
        Cloth,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )


class Cart(models.Model):
    cloth = models.ForeignKey(
        Cloth,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    size = models.CharField(
        max_length=2,  # Adjust the max_length as per your requirement
        choices=[
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
            # Add more choices if needed
        ],
        default='S'
    )
    quantity = models.PositiveIntegerField(
        default=1
    )
