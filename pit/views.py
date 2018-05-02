from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
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
from .models import Pet
from .forms import TransactionForm
from .forms import PetForm
from .models import Client
from .forms import ClientForm
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

def pets_view(request, pet_type):
    user = request.user
    pets = Pet.objects.filter(hidden=True, pet_type = pet_type)
    return render(request, 'pit/pet.html', {'pets': pets, 'username': user.username, 'pet_type': pet_type})

def pet_new(request, pet_type):
    if request.method == "POST":
        # form = PetForm(request.POST)
        try:
          pet = Pet()
          pet.name = request.POST.get("name","default_name")
          pet.picture_1 = request.POST.get("picture_1","http://")
          pet.picture_2 = request.POST.get("picture_2","http://")
          pet.picture_3 = request.POST.get("picture_3","http://")
          pet.description = request.POST.get("description","No description")
          pet.main_description = request.POST.get("main_description","No main description")
          pet.age = request.POST.get("age",1)
          pet.pet_type = pet_type
          pet.author = request.user
          pet.date = timezone.now()
          pet.save()
          return redirect('index')
        except:
          pass
    return render(request, 'pit/pet_edit.html')

def hidden_pet(request):
    user = request.user
    pets = Pet.objects.filter(hidden=False)
    return render(request, 'pit/hidden_pet.html', {'pets': pets, 'username': user.username})

def morepet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pit/more_pet.html', {'pet': pet})

def delete_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.hidden = False
    pet.save()
    return redirect('index')

def return_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.hidden = True
    pet.save()
    return redirect('hidden_pet')


def client(request):
    user = request.user
    clients = Client.objects.all
    return render(request, 'pit/client.html', {'clients': clients, 'username': user.username})


def client_new(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
      try:	
        client = Client()
        client.name = request.POST.get("name","default_name")
        client.number = request.POST.get("number", "-")
        client.pet_name = pet.name
        client.author = request.user
        client.date = timezone.now()
        client.save()
        return redirect('thanks')
      except:
        pass
    return render(request, 'pit/client_edit.html')


def thanks(request):
    return render(request, 'pit/thanks.html')



