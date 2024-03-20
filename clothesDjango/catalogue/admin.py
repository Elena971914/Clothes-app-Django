from django.contrib import admin

from clothesDjango.catalogue.models import Cloth


@admin.register(Cloth)
class AdminCloth(admin.ModelAdmin):
    list_display = ['type', 'name', 'price', 'stocked_S', 'stocked_M', 'stocked_L']
    list_filter = ['type', 'price', 'color']
    search_fields = ['type', 'name', 'color']
    fields = ['type', 'name', 'color', 'price', ('stocked_S', 'stocked_M', 'stocked_L')]