from django.shortcuts import render
from .forms import SearchForm
from .models import Search


def Search(request):
    item = Search.objects.all()
    context = {'item': item}
    return render(request, 'home.html', context)


def item_search(request):
    form_search = SearchForm()
    if request.method == 'POST':
        pass



