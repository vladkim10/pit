from django.db import models

# Create your models here.
class Dog(models.Model):
  name = models.CharField(max_length=1000,default="Sharik")
  breed = models.CharField(max_length=1000,default="Dvor")
  age = models.IntegerField(default=1)

  def __str__(self):
    return self.name

