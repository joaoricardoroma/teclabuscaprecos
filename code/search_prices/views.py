from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchForm, ClientForm
from .models import Search, Client


def search(request):
    clients = Client.objects.all()
    item = Search.objects.all()
    form_search = SearchForm()
    id_logado = 1
    searches = Search.objects.filter(client_id=id_logado)
    if request.method == 'POST':
        form_search = SearchForm(request.POST)

        if form_search.is_valid():
            form_search.save()
            return redirect('search_prices:search')
    context = {
        'item': item,
        'form_search': form_search,
        'searches': searches,
        'clients': clients,
               }
    return render(request, 'home.html', context)


def client_profile(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form_client = ClientForm(instance=client)

    if request.method == 'POST':
        form_client = ClientForm(request.POST, instance=client)

        if form_client.is_valid():
            form_client.save()
            return redirect('search_prices:client_profile', pk=client.id)
    context = {
        'client': client,
        'form_client': form_client,
    }
    return render(request, 'client_profile.html', context)


def register_client(request):
    client_form = ClientForm()
    if request.method == 'POST':
        client_form = ClientForm(request.POST)

        if client_form.is_valid():
            client_form.save()
            return redirect('search_prices:search')
    context = {
         'client_form': client_form
    }
    return render(request, 'register_client.html', context)


def delete_search(request, pk):
    search_client = get_object_or_404(Search, pk=pk)
    search_client.delete()
    return redirect('search_prices:search')


def delete_client(request, pk):
    delete_client = get_object_or_404(Client, pk=pk)
    delete_client.delete()
    return redirect('search_prices:search')
