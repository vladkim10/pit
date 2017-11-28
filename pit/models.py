from django.db import models

# Create your models here.
class Dog(models.Model):
  name = models.CharField(max_length=1000,default="Sharik")
  breed = models.CharField(max_length=1000,default="Dvor")

  def __str__(self):
    return self.name

