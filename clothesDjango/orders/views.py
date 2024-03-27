from django import views
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from django.shortcuts import render


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
    pass


class OrderDeleteView(DeleteView):
    pass

