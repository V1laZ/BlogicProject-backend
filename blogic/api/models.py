from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=9)
    PIN = models.CharField(max_length=20)
    age = models.IntegerField()

class Advisor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=9)
    PIN = models.CharField(max_length=20)
    age = models.IntegerField()

class Contract(models.Model):
    reg_num = models.CharField(max_length=10, primary_key=True)
    institution = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    manager = models.ForeignKey(Advisor, on_delete=models.PROTECT)
    date_close = models.DateField()
    date_valid = models.DateField()
    date_end = models.DateField()

