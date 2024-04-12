from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from clothesDjango.accounts.validators import validate_phone_number
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
    phone = models.CharField(max_length=10, validators=[validate_phone_number])
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
    agreed_to_terms = models.BooleanField(default=False)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    def save(self, *args, **kwargs):
        if (timezone.now() - self.date_of_purchase).days > 3:
            self.status = 'Sent'
        else:
            self.status = 'In Process'
        super().save(*args, **kwargs)


class CopiedCart(models.Model):
    cloth = models.ForeignKey(
        Cloth,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    size = models.CharField(
        max_length=2,
        choices=[
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large'),
        ],
        default='S'
    )
    quantity = models.PositiveIntegerField(
        default=1
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='copied_carts'
    )

    def subtotal(self):
        return self.quantity * self.cloth.price

    class Meta:
        verbose_name = "Copied Cart"
        verbose_name_plural = "Copied Carts"

