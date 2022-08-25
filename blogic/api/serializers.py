from rest_framework import  serializers
from .models import Client, Advisor, Contract

# Serializers define the API representation.
class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'PIN', 'age']

class PoradceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'PIN', 'age']

class SmlouvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['reg_num', 'institution', 'client', 'manager', 'date_close', 'date_valid', 'date_end']