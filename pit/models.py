from django.db import models
from django.utils import timezone
# Create your models here.
class Dog(models.Model):
  url = models.CharField(max_length=1000,default="", blank=True)
  name = models.CharField(max_length=1000,default="", blank=True)
  description = models.CharField(max_length=1000,default="", blank=True)
  date = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
    return self.name

class Transaction(models.Model):
  date = models.DateTimeField(default=timezone.now)
  description = models.CharField(max_length=1000, default="no description")
  amount = models.IntegerField(default=0)

  def __str__(self):
    return self.description + " " + str(self.amount) + " kzt"
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
