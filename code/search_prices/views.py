from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchForm
from .models import Search, Client


def search(request, pk):
    item = Search.objects.all()
    form_search = SearchForm()
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        client = get_object_or_404(Client, pk=pk)
        form_search = SearchForm(request.POST)
        form_search.instance.client = client

        if form_search.is_valid():
            form_search.save()
            return redirect('search_prices:search')
    context = {'item': item,
               'form_search': form_search,
               'client': client,
               }
    return render(request, 'home.html', context)


def searched_item(request):
    return render(request, 'searched_item.html')

