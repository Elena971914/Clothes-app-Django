from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clothesDjango.common.urls')),
    path('shop/', include('clothesDjango.catalogue.urls')),
    path('accounts/', include('clothesDjango.accounts.urls'))
]
