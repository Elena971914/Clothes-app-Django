from django.contrib import admin

from clothesDjango.accounts.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'get_all_orders']
    search_fields = ['first_name', 'last_name', 'email']

    def get_all_orders(self):
        return ', '.join([o.name for o in self.orders.all()])
