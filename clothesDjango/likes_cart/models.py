from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import View
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

    def subtotal(self):
        return self.quantity * self.cloth.price


class UpdateCartItemView(View):
    def post(self, request, pk_cart):
        cart_item = get_object_or_404(Cart, pk=pk_cart)
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        return redirect('view cart')
