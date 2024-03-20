from django.contrib import admin

from clothesDjango.common.models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author', 'rating', 'date_time']
    search_fields = ['author']
