from django.contrib.auth.decorators import permission_required
from django.urls import path

from clothesDjango.catalogue.views import show_shop, show_product_details, AddCloth

urlpatterns = [
    path('', show_shop, name='shop'),
    path('item/<int:pk>', show_product_details, name='show product details'),
    path('add-item/', permission_required('catalogue.add_cloth')(AddCloth.as_view()), name='add cloth'),
]
