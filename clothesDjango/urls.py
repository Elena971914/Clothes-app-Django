from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clothesDjango.common.urls')),
    path('shop/', include('clothesDjango.catalogue.urls')),
    path('accounts/', include('clothesDjango.accounts.urls')),
    path('favourites/', include('clothesDjango.likes_cart.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
