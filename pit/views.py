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
import math
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
        try:
          transaction = Transaction()
          transaction.description = request.POST.get("description","No description")
          transaction.amount = request.POST.get("amount", 0)
          transaction.author = request.user
          transaction.date = timezone.now()
          transaction.save()
          return redirect('kzt_list')
        except:
          pass
    return render(request, 'pit/transaction_edit.html')


def pet_new(request, pet_type):
    if request.method == "POST":
        try:
          pet = Pet()
          pet.name = request.POST.get("name","default_name")
          pet.picture_1 = request.POST.get("picture_1","http://")
          pet.picture_2 = request.POST.get("picture_2","http://")
          pet.picture_3 = request.POST.get("picture_3","http://")
          pet.description = request.POST.get("description","No description")
          pet.age = request.POST.get("age",1)
          pet.gender = request.POST.get("gender", "Самец")
          pet.pet_type = pet_type
          pet.author = request.user
          pet.date = timezone.now()
          pet.save()
          return redirect('pet_success')
        except:

          pass
    return render(request, 'pit/pet_edit.html')








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
    client_number = len(Client.objects.filter(hidden=True))
    return render(request, 'pit/index.html', {'username': user.username, 'client_number': client_number})

def pets_view(request, pet_type):
    page = int(request.GET.get("page",0))
    number = 8
    user = request.user
    pages = len(Pet.objects.filter(hidden=True, pet_type = pet_type))
    pages_links = [] 
    for i in range(math.ceil(pages/number)):
        pages_links.append("/pets/"+pet_type+"/?page="+str(i))


    pets = Pet.objects.filter(hidden=True, pet_type = pet_type)[page*number:page*number+number]
    return render(request, 'pit/pet.html', {'pets': pets, 'username': user.username, 'pet_type': pet_type, 'pages':pages_links})

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
          pet.age = request.POST.get("age",1)
          pet.gender = request.POST.get("gender", "Самец")
          pet.pet_type = pet_type
          pet.author = request.user
          pet.date = timezone.now()
          pet.save()
          return redirect('pet_success')
        except:
          pass
    return render(request, 'pit/pet_edit.html')

def hidden_pet(request):
    user = request.user
    pets = Pet.objects.filter(hidden=False)
    return render(request, 'pit/hidden_pet.html', {'pets': pets, 'username': user.username})

def morepet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pets = Pet.objects.all()
    pets_grouped = [[]]
    for pet1 in pets:
       if len(pets_grouped[-1]) >= 3:
          pets_grouped.append([])
       pets_grouped[-1].append(pet1)
    return render(request, 'pit/more_pet.html', {'pet': pet, 'pets': pets, 'pets_grouped': pets_grouped})

def delete_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.hidden = False
    pet.save()
    return redirect('hidden_pet')

def return_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.hidden = True
    pet.save()
    return redirect('hidden_pet')


def client(request):
    user = request.user
    clients = Client.objects.filter(hidden=True)
    return render(request, 'pit/client.html', {'clients': clients, 'username': user.username})

def hidden_client(request):
    user = request.user
    clients = Client.objects.filter(hidden=False)
    return render(request, 'pit/hidden_client.html', {'clients': clients, 'username': user.username})

def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.hidden = False
    client.save()
    return redirect('client')

def return_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.hidden = True
    client.save()
    return redirect('hidden_client')


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
    return render(request, 'pit/client_edit.html', {'pet': pet})


def thanks(request):
    return render(request, 'pit/thanks.html')

def condition(request):
    return render(request, 'pit/condition.html')

def pet_success(request):
    return render(request, 'pit/pet_edit_success.html')



