from django.conf.urls.static import static
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, logout, login, get_user_model
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from clothesDjango.accounts.forms import RegisterUserForm, ProfileEditForm
from clothesDjango.accounts.models import Profile

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
        # TODO: orders
        # context['pets'] = self.request.user.pet_set.all()

        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'profile-edit.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('profile_details')  # Redirect to profile details page
    model = Profile

    def get_object(self, queryset=None):
        # Get or create the profile object for the current user
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)


class ProfileDeleteView(views.DeleteView):
    # queryset = Profile.objects.all()
    template_name = "profile-delete.html"

