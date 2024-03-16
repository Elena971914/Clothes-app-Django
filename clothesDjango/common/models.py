from django.db import models


class Testimonial(models.Model):
    author = models.CharField(
        max_length=50)
    text = models.TextField(
        blank=False,
        null=False
    )
    date_time = models.DateTimeField(
        auto_now=True,
    )
    photo = models.ImageField(1)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])



