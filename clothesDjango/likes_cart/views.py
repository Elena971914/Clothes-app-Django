from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum, F
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View
from django.views.generic import ListView

from clothesDjango.catalogue.models import Cloth
from clothesDjango.likes_cart.models import Likes, Cart
from clothesDjango.orders.views import calculate_total_price


class ViewLikes(LoginRequiredMixin, ListView):
    template_name = 'view-likes.html'
    model = Likes

    def get_queryset(self):
        user_liked_items = Likes.objects.filter(user=self.request.user)
        return user_liked_items


class ViewCart(LoginRequiredMixin, ListView):
    template_name = 'view-cart.html'
    model = Cart

    def get_queryset(self):
        user_cart_items = Cart.objects.filter(user=self.request.user)
        return user_cart_items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_price = calculate_total_price(self.request.user)
        context['total_price'] = total_price
        return context


@login_required
def like_toggle(request, pk_cloth):
    cloth = get_object_or_404(Cloth, pk=pk_cloth)
    item = Likes.objects.filter(cloth=cloth, user=request.user).first()
    is_liked = False

    if item:
        item.delete()
    else:
        Likes.objects.create(cloth=cloth, user=request.user)
        is_liked = True

    request.session['is_liked'] = is_liked
    return redirect(request.META.get('HTTP_REFERER') + f"#current-{pk_cloth}")


@login_required
def add_to_cart(request, pk_cloth):
    if request.method == 'POST':
        try:
            cloth = Cloth.objects.get(pk=pk_cloth)
            size = request.POST.get('size')
            Cart.objects.create(cloth=cloth, user=request.user, size=size)
            return redirect(request.META.get('HTTP_REFERER') + f"#current-{pk_cloth}")
        except ObjectDoesNotExist as e:
            return render(request, '404.html', status=500)


@login_required
def delete_cart_item(request, pk_cart):
    cart_item = get_object_or_404(Cart, pk=pk_cart)
    cart_item.delete()
    return redirect('view cart')


class UpdateCartItemView(LoginRequiredMixin, View):
    def post(self, request, pk_cart):
        cart_item = get_object_or_404(Cart, pk=pk_cart)

        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            cloth = cart_item.cloth
            size = cart_item.size
            if (size == 'L' and cloth.stocked_L >= quantity) or \
                    (size == 'M' and cloth.stocked_M >= quantity) or \
                    (size == 'S' and cloth.stocked_S >= quantity):
                cart_item.quantity = quantity
                cart_item.save()
        return redirect('view cart')
