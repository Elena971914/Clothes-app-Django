from django.urls import path

from clothesDjango.catalogue.views import show_all_items

urlpatterns = [
    path('', show_all_items, name='show all' )
]