from django.urls import path

from clothesDjango.orders.views import ShowAllOrders, OrderCreateView, ShowOrderDetails

urlpatterns = [
        path('', ShowAllOrders.as_view(), name='show user orders'),
        path('create-order/', OrderCreateView.as_view(), name='create order'),
        path('show-order-details/<int:pk>', ShowOrderDetails.as_view(), name='order details')
]
