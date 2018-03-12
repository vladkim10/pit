from django import forms

from .models import Transaction

from .models import Dog

from .models import Cat

from .models import OtherPets

class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('description', 'amount')

class DogForm(forms.ModelForm):

    class Meta:
        model = Dog
        fields = ('url', 'name', 'description')

class CatForm(forms.ModelForm):

    class Meta:
        model = Cat
        fields = ('url', 'name', 'description')

class OtherPetsForm(forms.ModelForm):

    class Meta:
        model = OtherPets
        fields = ('url', 'name', 'description')
