from django.db import models

# Create your models here.
class Klient(models.Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    tel_cislo = models.CharField(max_length=9)
    rod_cislo = models.CharField(max_length=20)
    vek = models.IntegerField()

class Poradce(models.Model):
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    tel_cislo = models.CharField(max_length=9)
    rod_cislo = models.CharField(max_length=20)
    vek = models.IntegerField()

class Smlouva(models.Model):
    ev_cislo = models.CharField(max_length=10, primary_key=True)
    instituce = models.CharField(max_length=20)
    klient = models.ForeignKey(Klient, on_delete=models.PROTECT)
    spravce = models.ForeignKey(Poradce, on_delete=models.PROTECT)
    dat_uzavreni = models.DateField()
    dat_platnosti = models.DateField()
    dat_ukonceni = models.DateField()

