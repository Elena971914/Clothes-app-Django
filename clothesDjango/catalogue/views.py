from django.http import HttpResponse
from django.shortcuts import render


def show_shop(request):
    return render(request, 'shop.html')


def show_product_details(request, pk):
    return None
