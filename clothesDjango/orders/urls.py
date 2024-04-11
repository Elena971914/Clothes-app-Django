from django.urls import path

from clothesDjango.orders.views import OrderCreate, DeleteOrder, OrderDetails, ConfirmOrder

urlpatterns = [
        path('create-order/', OrderCreate.as_view(), name='create order'),
        path('confirm-order/', ConfirmOrder.as_view(), name='confirm order'),
        path('<int:pk>/', OrderDetails.as_view(), name='order details'),
        path('<int:pk>/delete', DeleteOrder.as_view(), name='delete order'),
]
