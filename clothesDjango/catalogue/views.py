from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from clothesDjango.catalogue.forms import SearchForm, AddClothForm
from clothesDjango.catalogue.models import Cloth


def show_shop(request):

    all_clothes = Cloth.objects.all()
    search_form = SearchForm()
    paginator = Paginator(all_clothes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_text = search_form.cleaned_data.get('search')
            all_clothes = all_clothes.filter(
                Q(type__icontains=search_text) |
                Q(color__icontains=search_text) |
                Q(name__icontains=search_text))
            paginator = Paginator(all_clothes, 2)
            page_obj = paginator.get_page(page_number)

    context = {
        'all_clothes': page_obj,
        'search_form': search_form,
        'page_obj': page_obj,
        'paginator': paginator
    }
    return render(request, 'shop.html', context)


def show_product_details(request, pk):
    cloth = Cloth.objects.get(pk=pk)
    context = {
        'cloth': cloth,
    }
    return render(request, 'product-details.html', context)


class AddCloth(CreateView):
    template_name = 'add-cloth.html'
    form_class = AddClothForm
    success_url = reverse_lazy('shop')

