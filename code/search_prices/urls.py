from django.urls import path
from . import views


app_name = 'search_prices'
urlpatterns = [
    path('', views.search, name='search'),
    path('client_register', views.register_client, name='register_client'),
    path('client_login', views.login_client, name='login_client'),
    path('logout_client', views.logout_client, name='logout_client'),
    path('<int:pk>/client_profile', views.client_profile, name='client_profile'),
    path('<int:pk>/delete', views.delete_search, name='delete_search'),
    path('<int:pk>/client_profile/delete', views.delete_client, name='delete_client'),
    ]
