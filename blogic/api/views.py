from rest_framework import viewsets
from .serializers import KlientSerializer, PoradceSerializer, SmlouvaSerializer
from .models import Client, Advisor, Contract

# ViewSets define the view behavior.
class KlientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = KlientSerializer

class PoradceViewSet(viewsets.ModelViewSet):
    queryset = Advisor.objects.all()
    serializer_class = PoradceSerializer

class SmlouvaViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = SmlouvaSerializer