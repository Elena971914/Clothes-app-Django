from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from .models import Newsletter, Testimonial
from .forms import NewsletterForm, TestimonialForm


from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def show_why(request):
    return render(request, 'why.html')


@login_required()
def show_contacts(request):
    return render(request, 'contact.html')


def show_testimonials(request):
    all_testimonials = Testimonial.objects.all()

    testimonial_form = TestimonialForm(request.POST or None, request.FILES or None)
    if testimonial_form.is_valid():
        testimonial_form.save()
        return redirect('testimonials')

    context = {
        'testimonial_form': testimonial_form,
        'all_testimonials': all_testimonials,
   }
    return render(request, 'testimonial.html', context)


@login_required
def edit_testimonial(request, pk):
    all_testimonials = Testimonial.objects.all()
    testimonial = Testimonial.objects.get(pk=pk)
    if request.method == 'GET':
        testimonial_edit_form = TestimonialForm(instance=testimonial, initial=testimonial.__dict__)
    else:
        testimonial_edit_form = TestimonialForm(request.POST, instance=testimonial)
        if testimonial_edit_form.is_valid():
            testimonial_edit_form.save()
            return redirect('testimonials')
    context = {
        'testimonial_edit_form': testimonial_edit_form,
        'all_testimonials': all_testimonials
    }
    return render(request, 'testimonial-edit.html', context)


@login_required()
def delete_testimonial(request, pk):
    testimonial = Testimonial.objects.get(pk=pk)
    testimonial.delete()
    return render(request, 'testimonial-delete.html')


def add_newsletter_user(request):
    newsletter_form = None
    email = None
    if request.method == 'GET':
        newsletter_form = NewsletterForm()
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            email = newsletter_form.cleaned_data['email']
            if not Newsletter.objects.filter(subscribed=email).exists():
                Newsletter.objects.create(subscribed=email)
            else:
                email = None
            return redirect('thank you newsletter', email)
    context = {
        'email': email,
        'all_subscribed': Newsletter.objects.all(),
        "newsletter_form": newsletter_form
    }
    return render(request, "newsletter-add.html", context)


def thank_you_newsletter(request, email):
    context = {'email': email}
    return render(request, 'newsletter.html', context)


def stop_newsletter_subscription(request, email):
    obj = Newsletter.objects.get(subscribed=email)
    context = {
        'ended_subscription': obj
    }
    obj.delete()
    return render(request, 'newsletter-end-subscription.html', context)
