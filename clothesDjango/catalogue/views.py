from django.http import HttpResponse
from django.shortcuts import render


def show_all_items(request):
    return HttpResponse('all')
