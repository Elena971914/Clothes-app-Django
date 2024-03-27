from django.core.validators import MinLengthValidator
from django.db import models


class Testimonial(models.Model):
    author = models.CharField(
        max_length=50)
    email = models.EmailField(
        null=False,
        blank=False
    )
    phone = models.CharField(
        max_length=10,
        null=True,
        blank=True
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

    #TODO: edit the unsubscribe button functionality





