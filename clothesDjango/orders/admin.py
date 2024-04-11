from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_of_purchase', 'id', 'user_full_name', 'total_price', 'status']
    list_filter = ['status', 'city']
    search_fields = ['user__first_name', 'user__last_name', 'phone']

    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}" if obj.user else "Unknown"

    user_full_name.short_description = 'User Full Name'

    def total_price(self, obj):
        return obj.calculate_total_price()

    total_price.short_description = 'Total Price'

    def status(self, obj):
        return obj.status
