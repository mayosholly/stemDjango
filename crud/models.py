from django.db import models

# Create your models here.

class Person(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=50)
    phonenumber= models.IntegerField()
    address= models.TextField(max_length=200)