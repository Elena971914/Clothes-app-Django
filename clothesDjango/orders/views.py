from django import views
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from django.shortcuts import render

from clothesDjango.orders.forms import OrderForm
from clothesDjango.orders.models import Order


class DisabledFormFieldsMixin:
    disabled_fields = ()

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'

        return form


class OrderDetail(DetailView):
    pass


class Orders(ListView):
    pass


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order-create.html'
    success_url = '/success/'  # Specify your success URL

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowAllOrders(ListView):
    pass


class ShowOrderDetails(DetailView):
    pass

