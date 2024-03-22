from django.http import HttpResponse
from django.shortcuts import render, redirect

from clothesDjango.common.forms import NewsletterForm
from clothesDjango.common.models import Newsletter


def index(request):
    email = None
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        if not Newsletter.objects.filter(subscribed=email).exists():
            Newsletter.objects.create(subscribed=email)
            return redirect('add newsletter user', email=email)
    context = {
        "newsletter_form": form,}
    return render(request, 'index.html', context)


def show_why(request):
    return render(request, 'why.html')


def show_contacts(request):
    return render(request, 'contact.html')


def show_testimonials(request):
    return render(request, 'contact.html')


def add_testimonial(request):
    return None


def edit_testimonial(request, pk):
    return None


def delete_testimonial(request, pk):
    return None


def add_newsletter_user(request, email):
    context = {
        'email': email,
        'all_subscribed': Newsletter.objects.all()
    }
    return render(request, "newsletter.html", context)

