from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_of_purchase', 'id', 'user_full_name', 'status', 'price']
    list_filter = ['status', 'city']
    search_fields = ['user__first_name', 'user__last_name', 'phone']

    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    user_full_name.short_description = 'User Full Name'
