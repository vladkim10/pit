from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction
from .models import Dog
from .forms import TransactionForm
from .forms import DogForm
import kkb
# Create your views here.


def kzt_list(request):
    transactions = Transaction.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'pit/kzt_list.html', {'transactions': transactions})

@csrf_exempt
def success(request):
    transaction = Transaction()
    transaction.description = "dumb"
    transaction.date = timezone.now()
    transaction.amount = 0
    transaction.save()
    if request.method == "POST":
      response = request.POST['response']
      result = kkb.postlink(response)
      if result.status:
         transaction = Transaction()
         transaction.description = result.data["CUSTOMER_NAME"]
         transaction.date = timezone.now()
         transaction.amount = int(result.data['ORDER_AMOUNT'])
         transaction.save()
         return render(request, 'pit/message.html', {'message': 'success!!! added ' + str(transaction.amount) + ' KZT!'})
      else:
         return render(request, 'pit/message.html', {'message': "we've got problem: " + result.message})
    return render(request, 'pit/message.html', {'message': "something strange"})

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
