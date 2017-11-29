from django.db import models
from django.utils import timezone
# Create your models here.
class Dog(models.Model):
  name = models.CharField(max_length=1000,default="Sharik")
  breed = models.CharField(max_length=1000,default="Dvor")
  age = models.IntegerField(default=1)

  def __str__(self):
    return self.name

class Transaction(models.Model):
  date = models.DateTimeField(default=timezone.now)
  description = models.CharField(max_length=1000, default="no description")
  amount = models.IntegerField(default=0)

  def __str__(self):
    return self.description + " " + str(self.amount) + " kzt"

