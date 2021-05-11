from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchForm
from .models import Search, Client


def search(request):
    item = Search.objects.all()
    form_search = SearchForm()
    id_logado = 1
    searches = Search.objects.filter(client_id=id_logado)
    if request.method == 'POST':
        form_search = SearchForm(request.POST)

        if form_search.is_valid():
            form_search.save()
            return redirect('search_prices:search')
    context = {'item': item,
               'form_search': form_search,
               'searches': searches,
               }
    return render(request, 'home.html', context)


def delete_search(request):
    id_logado = 1
    clients = Search.objects.filter(client_id=id_logado)
    clients.delete()
    return redirect('search_prices:search')
