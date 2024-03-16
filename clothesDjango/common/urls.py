from django.urls import path, include

from clothesDjango.common.views import index, show_why, show_contacts, show_testimonials, \
    add_testimonial, edit_testimonial, delete_testimonial

urlpatterns = [
    path('', index, name='index'),
    path('why/', show_why, name='why'),
    path('contacts/', show_contacts, name='contacts'),
    path('testimonials/', include([
        path('', show_testimonials, name='testimonials'),
        path('add/', add_testimonial, name='add testimonial'),
        path('<int:pk>/edit', edit_testimonial, name='edit testimonial'),
        path('<int:pk>/delete', delete_testimonial, name='delete testimonial'),
        ]))
]
