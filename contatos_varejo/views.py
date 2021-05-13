from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ContatoVarejoSerializer, CreateListModelMixin
from .models import ContatoVarejo

class ContatoVarejoViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    serializer_class = ContatoVarejoSerializer
    queryset = ContatoVarejo.objects.using('varejo').all()
