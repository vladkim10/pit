from django import forms

from .models import Transaction

from .models import Pet

from .models import Client

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('description', 'amount')

class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('picture_1', 'picture_2', 'picture_3', 'pet_type', 'name', 'description', 'main_description', 'age', 'gender', 'breed')


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'number')
