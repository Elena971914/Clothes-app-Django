from django.urls import path

from clothesDjango.catalogue.views import show_shop, show_product_details

urlpatterns = [
    path('', show_shop, name='shop'),
    path('item/<int:pk>', show_product_details, name='show product details')
]