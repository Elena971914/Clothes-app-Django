from django.urls import path, include

from clothesDjango.accounts.views import show_user_profile, show_user_orders, \
    edit_user_profile, delete_user_profile, RegisterUserView, LoginUserView, logout_user

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('my-profile/<int:pk>/', include([
        path('', show_user_profile, name='show user profile'),
        path('edit/', edit_user_profile, name='edit user profile'),
        path('delete/', delete_user_profile, name='show user profile'),
        path('my-orders/', show_user_orders, name='show user orders')]
    ))
]
