from django.http import HttpResponse
from django.shortcuts import render

from clothesDjango.catalogue.models import Cloth


def show_shop(request):
    all_clothes = Cloth.objects.all()
    context = {
        'all_clothes': all_clothes
    }
    return render(request, 'shop.html', context)


def show_product_details(request, pk):
    cloth = Cloth.objects.get(pk=pk)
    context = {
        'cloth': cloth
    }
    return render(request, 'product-details.html', context)
