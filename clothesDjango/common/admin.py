from django.contrib import admin

from clothesDjango.common.models import Testimonial, Newsletter


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'rating']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['subscribed']
