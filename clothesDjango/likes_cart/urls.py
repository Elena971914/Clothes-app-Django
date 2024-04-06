from django.urls import path, include

from clothesDjango.likes_cart.views import ViewLikes, ViewCart, like_toggle, delete_cart_item, add_to_cart

urlpatterns = [
    path("like/<int:pk_cloth>/", like_toggle, name="like"),
    path("add_to_cart/<int:pk_cloth>/", add_to_cart, name="add to cart"),
    path('my-likes/', ViewLikes.as_view(), name='view likes'),
    path('my-cart/', ViewCart.as_view(), name='view cart'),
    path('my-cart/<int:pk_cart>/delete', delete_cart_item, name='delete cart item')
]
