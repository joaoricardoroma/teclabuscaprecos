from django.urls import path
from . import views


app_name = 'search_prices'
urlpatterns = [
    path('', views.search, name='search'),
    path('delete', views.delete_search, name='delete_search'),
    ]
