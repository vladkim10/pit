from django.contrib import admin
from pit.models import Dog
from pit.models import Transaction
from pit.models import Cat
from pit.models import OtherPets
# Register your models here.
admin.site.register(Dog)
admin.site.register(Transaction)
admin.site.register(Cat)
admin.site.register(OtherPets)
