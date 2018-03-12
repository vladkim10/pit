from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from .models import Transaction
from .models import Dog
from .forms import TransactionForm
from .forms import DogForm
from .models import Cat
from .forms import CatForm
from .models import OtherPets
from .forms import OtherPetsForm
import kkb
# Create your views here.

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "pit/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


def kzt_list(request):
    user = request.user
    transactions = Transaction.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'pit/kzt_list.html', {'transactions': transactions, 'username': user.username})

@csrf_exempt
def success(request):
    if request.method == "POST":
      response = request.POST['response']
      result = kkb.postlink(response)
      if result.status:
         transaction = Transaction()
         transaction.description = result.data["CUSTOMER_NAME"]
         transaction.date = timezone.now()
         transaction.amount = int(float(result.data["ORDER_AMOUNT"]))
         transaction.save()
         return render(request, 'pit/message.html', {'message': 'success!!! added ' + str(transaction.amount) + ' KZT!'})
      else:
         return render(request, 'pit/message.html', {'message': "we've got problem: " + result.message})
    return render(request, 'pit/message.html', {'message': "something strange"})

def index(request):
    user = request.user
    return render(request, 'pit/index.html', {'username': user.username})


def dog(request):
    user = request.user
    dogs = Dog.objects.all()
    return render(request, 'pit/dog.html', {'dogs': dogs, 'username': user.username})

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
            return redirect('dog')
    else:
        form = DogForm()
    return render(request, 'pit/dog_edit.html', {'form': form})

def cat(request):
    user = request.user
    cat = Cat.objects.all()
    return render(request, 'pit/cat.html', {'cat': cat, 'username': user.username})

def cat_new(request):
    if request.method == "POST":
        form = CatForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.author = request.user
            cat.date = timezone.now()
            cat.save()
            return redirect('cat')
    else:
        form = CatForm()
    return render(request, 'pit/cat_edit.html', {'form': form})

def otherPets(request):
    user = request.user
    otherPets = OtherPets.objects.all()
    return render(request, 'pit/otherPets.html', {'otherPets': otherPets, 'username': user.username})

def otherPets_new(request):
    if request.method == "POST":
        form = OtherPetsForm(request.POST)
        if form.is_valid():
            otherPets = form.save(commit=False)
            otherPets.author = request.user
            otherPets.date = timezone.now()
            otherPets.save()
            return redirect('otherPets')
    else:
        form = OtherPetsForm()
    return render(request, 'pit/otherPets_edit.html', {'form': form})
