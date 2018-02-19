from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Transaction
from .models import Dog
from .forms import TransactionForm
from .forms import DogForm
import kkb
# Create your views here.

def kkb_init(request):
    kkb_context = kkb.get_context(order_id = '333',amount="666")
    return render(request, 'kkb.html', context = {kkb_context: kkb_context})

