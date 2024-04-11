from django.conf.urls.static import static
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, logout, login, get_user_model
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from clothesDjango.accounts.forms import RegisterUserForm, ProfileEditForm
from clothesDjango.accounts.models import Profile
from clothesDjango.orders.models import Order

UserModel = get_user_model()


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


#                        PROFILE VIEWS              PROFILE VIEWS
class ProfileDetailsView(views.DetailView):

    template_name = "profile-details.html"
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        orders = Order.objects.filter(user=user).order_by('-date_of_purchase')
        context['orders'] = orders

        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'profile-edit.html'
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy('show user profile', kwargs={'pk': self.request.user.pk})

    def get_object(self, queryset=None):
        # Return the current user instance
        return self.request.user

    def form_valid(self, form):
        # Save the form data directly to the user instance
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)

    def get_initial(self):
        # Get initial data for the form
        initial = super().get_initial()
        user = self.request.user
        initial['email'] = user.email
        initial['username'] = user.username
        initial['first_name'] = user.first_name
        initial['last_name'] = user.last_name
        initial['date_of_birth'] = user.date_of_birth
        initial['phone_number'] = user.phone_number
        initial['address'] = user.address
        return initial


class ProfileDeleteView(views.DeleteView):
    # queryset = Profile.objects.all()
    template_name = "profile-delete.html"

