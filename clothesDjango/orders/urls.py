from django.contrib.auth.decorators import permission_required
from django.urls import path

from clothesDjango.orders.views import OrderCreate, DeleteOrder, OrderDetails, ConfirmOrder, show_all_orders

urlpatterns = [
        path('show-all/', show_all_orders, name='show all orders'),
        path('create-order/', OrderCreate.as_view(), name='create order'),
        path('confirm-order/', ConfirmOrder.as_view(), name='confirm order'),
        path('<int:pk>/', OrderDetails.as_view(), name='order details'),
        path('<int:pk>/delete', DeleteOrder.as_view(), name='delete order'),
]
