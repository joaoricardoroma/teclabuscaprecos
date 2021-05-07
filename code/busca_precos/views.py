from django.shortcuts import render
from .models import Busca


def busca(request):
    item = Busca.objects.all()
    context = {'item': item}
    return render(request, 'home.html', context)

