from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchForm, RegisterForm, LoginForm
from .models import Search, Client
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

User = get_user_model()


class UserListView(ListView):
    template_name = 'registration/user_list.html'
    queryset = User.objects.all()


class UserUpdateView(UpdateView):
    model = User
    template_name = 'register_client.html'
    form_class = RegisterForm
    success_url = '/'


def search(request):
    item = Search.objects.all()
    form_search = SearchForm()
    id_logado = 1
    searches = Search.objects.filter(client_id=id_logado)
    if request.method == 'POST':
        form_search = SearchForm(request.POST)

        if form_search.is_valid():
            form_search.save()
            return redirect('search_prices:search')

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(User, id=id_)

    context = {
        'item': item,
        'form_search': form_search,
        'searches': searches,
    }
    return render(request, 'home.html', context)


def register_client(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")

        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None

        if user is not None:
            login(request, user)
            return redirect("search_prices:search")
        else:
            request.session['register_error'] = 1

    context = {
        "form": form
    }
    return render(request, "register_client.html", context)


# def register_client(request):
#     client_form = ClientForm()
#     if request.method == 'POST':
#         client_form = ClientForm(request.POST)
#
#         if client_form.is_valid():
#             client_form.save()
#             return redirect('search_prices:search')
#     context = {
#          'client_form': client_form
#     }
#     return render(request, 'register_client.html', context)


def login_client(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        client = authenticate(request, username=username, password=password)
        if client is not None:
            login(request, client)
            return redirect("/")
        else:
            request.session['invalid_user'] = 1

    context = {
        "form": form
    }
    return render(request, "login_client.html", context)


def logout_client(request):
    logout(request)
    return redirect("/")


def delete_search(request, pk):
    search_client = get_object_or_404(Search, pk=pk)
    search_client.delete()
    return redirect('search_prices:search')


def delete_client(request, pk):
    delete_client = get_object_or_404(Client, pk=pk)
    delete_client.delete()
    return redirect('search_prices:search')
