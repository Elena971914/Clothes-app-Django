from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from clothesDjango.catalogue.forms import SearchForm, AddClothForm, UpdateClothForm
from clothesDjango.catalogue.models import Cloth
from django.core.cache import cache


# TODO - add filtering of the objects and sorting
def show_shop(request):
    if not cache.get('all_clothes'):
        cache.set('all_clothes', Cloth.objects.all(), 60)

    all_clothes = cache.get('all_clothes')
    search_form = SearchForm()
    paginator = Paginator(all_clothes, 8)
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
    try:
        cloth = get_object_or_404(Cloth, pk=pk)

        previously_viewed = request.session.get('previously_viewed', [])
        if cloth.pk in previously_viewed:
            previously_viewed.remove(cloth.pk)
        previously_viewed.append(cloth.pk)

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
    except Exception as e:
        return render(request, '404.html', {'error_message': 'An error occurred. Please try again later.'})


class AddCloth(LoginRequiredMixin, CreateView):
    template_name = 'add-cloth.html'
    form_class = AddClothForm
    success_url = reverse_lazy('shop')


class UpdateCloth(LoginRequiredMixin, UpdateView):
    template_name = 'add-cloth.html'
    form_class = UpdateClothForm

    def get_object(self, queryset=None):
        try:
            return Cloth.objects.get(pk=self.kwargs['pk'])
        except Cloth.DoesNotExist:
            raise Http404("Cloth does not exist")

    def get_success_url(self):
        return reverse('show product details', kwargs={'pk': self.object.pk})
