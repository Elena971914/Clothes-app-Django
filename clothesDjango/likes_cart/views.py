from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from clothesDjango.catalogue.models import Cloth
from clothesDjango.likes_cart.models import Likes, Cart


class ViewLikes(ListView, LoginRequiredMixin):
    template_name = 'view-likes.html'
    model = Likes

    def get_queryset(self):
        user_liked_items = Likes.objects.filter(user=self.request.user)
        return user_liked_items


class ViewCart(ListView, LoginRequiredMixin):
    template_name = 'view-cart.html'
    model = Cart

    def get_queryset(self):
        user_cart_items = Cart.objects.filter(user=self.request.user)
        return user_cart_items


@login_required
def toggle_item(request, model_class, pk_cloth):
    cloth = get_object_or_404(Cloth, pk=pk_cloth)
    item = model_class.objects.filter(cloth=cloth, user=request.user).first()
    if item:
        item.delete()
    else:
        model_class.objects.create(cloth=cloth, user=request.user)

    return redirect(request.META.get('HTTP_REFERER') + f"#current-{pk_cloth}")


@login_required
def like_toggle(request, pk_user, pk_cloth):
    return toggle_item(request, Likes, pk_cloth)


@login_required
def cart_toggle(request, pk_user, pk_cloth):
    return toggle_item(request, Cart, pk_cloth)
