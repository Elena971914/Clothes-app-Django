from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, Sum
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, DeleteView, FormView
from django.shortcuts import render

from clothesDjango.likes_cart.models import Cart
from clothesDjango.orders.forms import OrderForm
from clothesDjango.orders.models import Order, CopiedCart


def calculate_total_price(user):
    """
    Calculate the total price of the cart items for a given user.
    """
    cart_items = Cart.objects.filter(user=user).annotate(subtotal=F('cloth__price') * F('quantity'))
    total_price = cart_items.aggregate(total_price=Sum('subtotal'))
    return total_price['total_price']


class OrderDetails(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'order-details.html'


class DeleteOrder(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'order-details.html'

    def get_success_url(self):
        return reverse_lazy('show user profile', kwargs={'pk': self.request.user.pk})


class OrderCreate(LoginRequiredMixin, FormView):
    template_name = 'order-create.html'
    success_url = reverse_lazy('confirm order')

    def get_form_class(self):
        return OrderForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_price'] = calculate_total_price(self.request.user)
        return context


class ConfirmOrder(LoginRequiredMixin, View):
    template_name = 'order-confirm.html'

    def post(self, request):
        form = OrderForm(request.user, request.POST)
        if form.is_valid():
            cart_items = Cart.objects.filter(user=request.user)
            total_price = calculate_total_price(request.user)

            order = Order.objects.create(
                user=request.user,
                phone=form.cleaned_data['phone'],
                delivery_address=form.cleaned_data['delivery_address'],
                city=form.cleaned_data['city'],
                postal_code=form.cleaned_data['postal_code'],
                is_personal_address=form.cleaned_data['is_personal_address'],
                payment_method=form.cleaned_data['payment_method'],
                comment=form.cleaned_data['comment'],
                price=total_price
            )

            for cart_item in cart_items:
                CopiedCart.objects.create(
                    cloth=cart_item.cloth,
                    user=cart_item.user,
                    size=cart_item.size,
                    quantity=cart_item.quantity,
                    order=order
                )
                cloth = cart_item.cloth
                if cart_item.size == 'S':
                    cloth.stocked_S -= cart_item.quantity
                elif cart_item.size == 'M':
                    cloth.stocked_M -= cart_item.quantity
                elif cart_item.size == 'L':
                    cloth.stocked_L -= cart_item.quantity
                cloth.save()
            cart_items.delete()

            return render(request, self.template_name, {'order': order})

        else:
            context = {
                'form': form,
                'total_price': calculate_total_price(request.user)
            }
            return render(request, 'order-create.html', context)


@login_required
def show_all_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'show-all-orders.html', context)
