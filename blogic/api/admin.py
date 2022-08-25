from django.contrib import admin
from .models import Client, Advisor, Contract


# Register your models here.
admin.site.register(Client)
admin.site.register(Advisor)
admin.site.register(Contract)