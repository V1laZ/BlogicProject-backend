from rest_framework import viewsets
from .serializers import KlientSerializer, PoradceSerializer, SmlouvaSerializer
from .models import Klient, Poradce, Smlouva

# ViewSets define the view behavior.
class KlientViewSet(viewsets.ModelViewSet):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

class PoradceViewSet(viewsets.ModelViewSet):
    queryset = Poradce.objects.all()
    serializer_class = PoradceSerializer

class SmlouvaViewSet(viewsets.ModelViewSet):
    queryset = Smlouva.objects.all()
    serializer_class = SmlouvaSerializer