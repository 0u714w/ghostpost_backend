from django.shortcuts import render
from rest_framework import viewsets
from ghostpost_backend.serializers import BaRSerializer
from ghostpost_backend.models import BoastsAndRoasts

class BaRView(viewsets.ModelViewSet):
    serializer_class = BaRSerializer
    queryset = BoastsAndRoasts.objects.all()