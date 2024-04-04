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
