from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from clothesDjango.catalogue.models import Cloth
from clothesDjango.likes_cart.models import Cart

UserModel = get_user_model()


class Order(models.Model):
    STATUS_CHOICES = (
        ('In Process', 'In Process'),
        ('Sent', 'Sent'),
    )
    PAYMENT_METHOD_CHOICES = (
        ('CARD', 'Card payment'),
        ('CASH', 'Cash on delivery'),
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    carts = models.ManyToManyField(Cart)
    phone = models.CharField(max_length=10)
    date_of_purchase = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='In Process')
    delivery_address = models.CharField(max_length=100)
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True)
    postal_code = models.CharField(
        max_length=100,
        blank=True,
        null=True)
    is_personal_address = models.BooleanField(default=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='CASH')
    comment = models.TextField()

    def save(self, *args, **kwargs):
        if (timezone.now() - self.date_of_purchase).days > 3:
            self.status = 'Sent'
        else:
            self.status = 'In Process'
        super().save(*args, **kwargs)

    def calculate_total_price(self):
        total_price = 0
        for cart in self.carts.all():
            total_price += cart.subtotal()
        return total_price
