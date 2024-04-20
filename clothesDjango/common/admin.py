from django.contrib import admin

from clothesDjango.common.models import Testimonial, Newsletter


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    pass