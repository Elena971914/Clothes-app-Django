from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Testimonial(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    text = models.TextField(
        blank=False,
        null=False,
        validators=[MinLengthValidator(5)]
    )
    date_time = models.DateTimeField(
        auto_now=True,
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to='testimonial_images'
    )
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)]
    )


class Newsletter(models.Model):
    subscribed = models.CharField(
        max_length=20,
        unique=True
    )






