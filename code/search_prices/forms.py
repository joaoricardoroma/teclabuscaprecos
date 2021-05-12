from django.forms import ModelForm
from .models import Search, Client


class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = '__all__'


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
