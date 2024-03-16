from django.urls import path, include

from clothesDjango.accounts.views import login_user, register_user, show_user_profile, show_user_orders, \
    edit_user_profile, delete_user_profile

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('my-profile/<int:pk>/', include([
        path('', show_user_profile, name='show user profile'),
        path('edit/', edit_user_profile, name='edit user profile'),
        path('delete/', delete_user_profile, name='show user profile'),
        path('my-orders/', show_user_orders, name='show user orders')]
    ))
]
