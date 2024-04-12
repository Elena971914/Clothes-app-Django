from django import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, Sum
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, DeleteView, FormView
from django.shortcuts import render, redirect, get_object_or_404

from clothesDjango.likes_cart.models import Cart
from clothesDjango.orders.forms import OrderForm
from clothesDjango.orders.models import Order


class DisabledFormFieldsMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'

        return form


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
        cart_items = Cart.objects.filter(user=self.request.user).annotate(subtotal=F('cloth__price') * F('quantity'))
        total_price = cart_items.aggregate(total_price=Sum('subtotal'))
        context['total_price'] = total_price['total_price']
        return context

    def form_invalid(self, form):
        print(form.errors)
        return redirect('create order', {'form': form})


class ConfirmOrder(View):
    template_name = 'order-confirm.html'

    def post(self, request):
        form = OrderForm(request.user, request.POST)
        if form.is_valid():
            cart_items = Cart.objects.filter(user=request.user)
            order = Order(
                user=request.user,
                phone=form.cleaned_data['phone'],
                delivery_address=form.cleaned_data['delivery_address'],
                city=form.cleaned_data['city'],
                postal_code=form.cleaned_data['postal_code'],
                is_personal_address=form.cleaned_data['is_personal_address'],
                payment_method=form.cleaned_data['payment_method'],
                comment=form.cleaned_data['comment']
            )
            order.save()
            order.carts.set(cart_items)
            return render(request, self.template_name, {'order': order, 'order_confirmed': True})
        else:
            return render(request, 'order-create.html', {'form': form, 'order_confirmed': False})
