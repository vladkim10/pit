from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Transaction
from .forms import TransactionForm
import kkb
import random
# Create your views here.

def kkb_init(request):

    if request.method == "POST":
        order_id = "".join([str(random.randint(0, 9)) for i in range(random.randint(10, 15))])
        kkb_context = kkb.get_context(order_id = order_id, amount=str(request.POST["price"]), currency_id="398")
        return render(request, 'kkb.html', context = {"kkb_context": kkb_context, "order_id": order_id, "price": request.POST["price"]})
    
    
    return render(request, 'kkb_form.html', context = {})

