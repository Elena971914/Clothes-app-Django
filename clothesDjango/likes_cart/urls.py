from django.urls import path

from clothesDjango.likes_cart.views import ViewLikes, ViewCart, like_toggle, cart_toggle

urlpatterns = [
    path("<int:pk_user>/like/<int:pk_cloth>/", like_toggle, name="like"),
    path("<int:pk_user>/add_to_cart/<int:pk_cloth>/", cart_toggle, name="add to cart"),
    path('<int:pk_user>/my-likes/', ViewLikes.as_view(), name='view likes'),
    path('<int:pk_user>/my-cart/', ViewCart.as_view(), name='view cart'),
]