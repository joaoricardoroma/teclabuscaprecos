from django.contrib import admin

from .models import Client
from .models import Search

admin.site.register(Client)
admin.site.register(Search)
