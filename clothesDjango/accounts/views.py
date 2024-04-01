from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, logout, login
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from clothesDjango.accounts.forms import RegisterUserForm


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('shop')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        # TODO
        # Send email on successful register: Variant 1
        # Not good one, only sends email when user is registered from the site,
        # but not from the `admin`
        # send_mail....

        return result

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('shop')


def logout_user(request):
    logout(request)
    return redirect('index')


def show_user_profile(request, pk):
    return None


def edit_user_profile(request, pk):
    return None


def delete_user_profile(request, pk):
    return None


def show_user_orders(request, pk):
    return None
