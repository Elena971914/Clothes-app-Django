from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


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

