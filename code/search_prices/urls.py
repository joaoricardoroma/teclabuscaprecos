from django.urls import path
from . import views
from .views import UserListView, UserUpdateView

app_name = 'search_prices'
urlpatterns = [
    path('', views.search, name='search'),
    path('list', UserListView.as_view(), name='UserListView'),
    path('register', views.register_client, name='register_client'),
    path('login', views.login_client, name='login_client'),
    path('logout', views.logout_client, name='logout_client'),
    path('<int:id>/profile', UserUpdateView.as_view(), name='UserUpdateView'),
    path('<int:pk>/delete', views.delete_search, name='delete_search'),
    path('<int:pk>/profile/delete', views.delete_client, name='delete_client'),
    ]
