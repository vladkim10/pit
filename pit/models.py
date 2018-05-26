from django.db import models
from django.utils import timezone
# Create your models here.

class Pet(models.Model):
  pet_type = models.CharField(max_length=100, default = "")
  picture_1 = models.CharField(max_length=1000,default="", blank=True)
  picture_2 = models.CharField(max_length=1000,default="", blank=True)
  picture_3 = models.CharField(max_length=1000,default="", blank=True)
  name = models.CharField(max_length=1000,default="", blank=True)
  description = models.TextField(default="")
  age = models.CharField(max_length=1000,default="", blank=True)
  gender_choices = (
    ('Самец', 'Самец'),
    ('Самка', 'Самка'),
  )
  gender = models.CharField(max_length=100, choices = gender_choices)
  breed = models.CharField(max_length=100,default="", blank=True)
  date = models.DateTimeField(default=timezone.now)
  hidden = models.BooleanField(default=True)
    
  def __str__(self):
    return self.name

class Transaction(models.Model):
  date = models.DateTimeField(default=timezone.now)
  description = models.TextField()
  amount = models.IntegerField()

  def __str__(self):
    return self.description + " " + str(self.amount) + " kzt"


class Client(models.Model):
  pet_name = models.CharField(max_length=100, default = "")
  name = models.CharField(max_length=100,default="", blank=True)
  number = models.CharField(max_length=100,default="", blank=True)
  date = models.DateTimeField(default=timezone.now)
  hidden = models.BooleanField(default=True)

  def __str__(self):
    return self.name
