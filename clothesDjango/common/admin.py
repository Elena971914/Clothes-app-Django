from django.contrib import admin

from clothesDjango.common.models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass
