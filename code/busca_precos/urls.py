from django.urls import path
from . import views


app_name = 'busca_precos'
urlpatterns = [
    path('', views.busca, name='busca'),
    ]