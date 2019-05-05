
# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import GameBarSerializer   # add this
from .models import GameBar                  # add this
        
class GameBarView(viewsets.ModelViewSet):       # add this
  serializer_class = GameBarSerializer          # add this
  queryset = GameBar.objects.all()              # add this