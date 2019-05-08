from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import BarSerializer, GameSerializer, ProductSerializer, ParticipantSerializer   # add this
from .models import Bar, Product, Participant, Game                  # add this
        
class BarView(viewsets.ModelViewSet):       
  serializer_class = BarSerializer          
  queryset = Bar.objects.all()              

class ProductView(viewsets.ModelViewSet):       
  serializer_class = ProductSerializer          
  queryset = Product.objects.all()              
class ParticipantView(viewsets.ModelViewSet):       
  serializer_class = ParticipantSerializer          
  queryset = Participant.objects.all()              
class GameView(viewsets.ModelViewSet):       
  serializer_class = GameSerializer          
  queryset = Game.objects.all()              