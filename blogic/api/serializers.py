from rest_framework import  serializers
from .models import Klient, Poradce, Smlouva

# Serializers define the API representation.
class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['id', 'jmeno', 'prijmeni', 'email', 'tel_cislo', 'rod_cislo', 'vek']

class PoradceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poradce
        fields = ['id', 'jmeno', 'prijmeni', 'email', 'tel_cislo', 'rod_cislo', 'vek']

class SmlouvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smlouva
        fields = ['ev_cislo', 'instituce', 'klient', 'spravce', 'dat_uzavreni', 'dat_platnosti', 'dat_ukonceni']