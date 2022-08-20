from django.contrib import admin
from .models import Klient, Poradce, Smlouva


# Register your models here.
admin.site.register(Klient)
admin.site.register(Poradce)
admin.site.register(Smlouva)