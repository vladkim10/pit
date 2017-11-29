from django.shortcuts import render
from django.utils import timezone
from .models import Transaction
# Create your views here.
def kzt_list(request):
    transactions = Transaction.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'pit/kzt_list.html', {'transactions': transactions})
