from django.contrib import admin
from pit.models import Pet
from pit.models import Transaction
from pit.models import Client
# Register your models here.
admin.site.register(Pet)
admin.site.register(Transaction)
admin.site.register(Client)
