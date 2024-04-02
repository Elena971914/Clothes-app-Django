from django.urls import path, include

from clothesDjango.accounts.views import RegisterUserView, LoginUserView, logout_user, \
    ProfileEditView, ProfileDeleteView, ProfileDetailsView
from clothesDjango.orders.views import OrderCreateView


urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('my-profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='show user profile'),
        path('edit/', ProfileEditView.as_view(), name='edit user profile'),
        path('delete/', ProfileDeleteView.as_view(), name='show user profile'),
        path('my-orders/', include('clothesDjango.orders.urls'))]
    ))
]
