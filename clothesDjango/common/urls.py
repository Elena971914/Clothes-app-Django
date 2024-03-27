from django.urls import path, include

from clothesDjango.common.views import index, show_why, show_contacts, show_testimonials, \
    edit_testimonial, delete_testimonial, add_newsletter_user, thank_you_newsletter, \
    stop_newsletter_subscription

urlpatterns = [
    path('', index, name='index'),
    path('why/', show_why, name='why'),
    path('contacts/', show_contacts, name='contacts'),
    path('testimonials/', include([
        path('', show_testimonials, name='testimonials'),
        path('<int:pk>/edit', edit_testimonial, name='edit testimonial'),
        path('<int:pk>/delete', delete_testimonial, name='delete testimonial'),
        ])),
    path('newsletter/', include([
        path('', add_newsletter_user, name='add newsletter user'),
        path('<email>', thank_you_newsletter, name='thank you newsletter'),
        path('<email>/stop', stop_newsletter_subscription, name='stop subscription')
    ]))
]
