from django.urls import path
from . import views


app_name = 'search_prices'
urlpatterns = [
    path('', views.search, name='search'),
    path('search', views.search, name='searched_item'),
    ]
