from django import forms

from .models import Transaction

from .models import Dog

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('description', 'amount')

class DogForm(forms.ModelForm):

    class Meta:
        model = Dog
        fields = ('url', 'name', 'description')
