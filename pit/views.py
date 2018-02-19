from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Transaction
from .models import Dog
from .forms import TransactionForm
from .forms import DogForm
# Create your views here.

def kzt_list(request):
    transactions = Transaction.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'pit/kzt_list.html', {'transactions': transactions})


def index(request):
    dogs = Dog.objects.all()
    return render(request, 'pit/index.html', {'dogs': dogs})

def transaction_new(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.author = request.user
            transaction.date = timezone.now()
            transaction.save()
            return redirect('kzt_list')
    else:
        form = TransactionForm()
    return render(request, 'pit/transaction_edit.html', {'form': form})

def dog_new(request):
    if request.method == "POST":
        form = DogForm(request.POST)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.author = request.user
            dog.date = timezone.now()
            dog.save()
            return redirect('index')
    else:
        form = DogForm()
    return render(request, 'pit/dog_edit.html', {'form': form})
