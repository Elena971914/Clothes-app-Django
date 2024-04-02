from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from clothesDjango.catalogue.models import Cloth

UserModel = get_user_model()


class Order(models.Model):
    STATUS_CHOICES = (
        ('IN_PROCESS', 'In Process'),
        ('SEND', 'Send'),
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    date_of_purchase = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='IN_PROCESS')
    delivery_address = models.CharField(max_length=100)
    is_personal_address = models.BooleanField(default=True)
    payment_method = models.CharField(max_length=20)
    comment = models.TextField()

    def save(self, *args, **kwargs):
        # Automatically set the status based on the date of purchase
        if (timezone.now() - self.date_of_purchase).days > 3:
            self.status = 'SEND'
        else:
            self.status = 'IN_PROCESS'
        super().save(*args, **kwargs)