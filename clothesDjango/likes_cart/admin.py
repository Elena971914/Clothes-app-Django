from django.contrib import admin

from clothesDjango.likes_cart.models import Likes, Cart


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

