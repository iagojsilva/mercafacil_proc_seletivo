from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ContatoMacapaSerializer, CreateListModelMixin
from .models import ContatoMacapa

class ContatoMacapaViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    serializer_class = ContatoMacapaSerializer
    queryset = ContatoMacapa.objects.using('macapa').all()
