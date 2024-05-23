from django.db import models

# Create your models here.
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)

class Consumer(models.Model):
    name = models.CharField(max_length=255)

class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    consumers = models.ManyToManyField(Consumer)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)