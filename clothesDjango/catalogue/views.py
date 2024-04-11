from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from clothesDjango.catalogue.forms import SearchForm, AddClothForm
from clothesDjango.catalogue.models import Cloth
from django.core.cache import cache


# TODO - add filtering of the objects and sorting
def show_shop(request):
    if not cache.get('all_clothes'):
        cache.set('all_clothes', Cloth.objects.all(), 60)

    all_clothes = cache.get('all_clothes')
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

    previously_viewed = request.session.get('previously_viewed', [])

    if cloth.pk in previously_viewed:
        previously_viewed.remove(cloth.pk)
    previously_viewed.append(cloth.pk)
    # TODO check if works correct with new user
    if len(previously_viewed) < 4:
        previously_viewed_slice = previously_viewed[:-1]
    else:
        previously_viewed_slice = previously_viewed[-4:-1]

    previously_viewed_clothes = Cloth.objects.filter(pk__in=previously_viewed_slice)

    request.session['previously_viewed'] = previously_viewed

    context = {
        'cloth': cloth,
        'previously_viewed_clothes': previously_viewed_clothes,
    }

    return render(request, 'product-details.html', context)


class AddCloth(CreateView):
    template_name = 'add-cloth.html'
    form_class = AddClothForm
    success_url = reverse_lazy('shop')

