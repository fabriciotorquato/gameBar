from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import BarSerializer, GameSerializer, ProductSerializer, ParticipantSerializer   # add this
from .models import Bar, Product, Participant, Game                  # add this
from rest_framework.response import Response
from rest_framework import status

class BarView(viewsets.ModelViewSet):    
  """
  retrieve:
      Return the given Bar.

  list:
      Return a list of all Bars.

  create:
      Create a new Bar.

  destroy:
      Delete a bar.

  update:
      Update a bar.

  partial_update:
      Update a bar.
  """   
  serializer_class = BarSerializer          
  queryset = Bar.objects.all()         
       
  def destroy(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      instance.status = False
      instance.save()
    except Http404:
        pass
    return Response(status=status.HTTP_204_NO_CONTENT)  

class ProductView(viewsets.ModelViewSet):       
  """
  retrieve:
      Return the given Product.

  list:
      Return a list of all Products.

  create:
      Create a new Product.

  destroy:
      Delete a Product.

  update:
      Update a Product.

  partial_update:
      Update a Product.
  """   
  serializer_class = ProductSerializer          
  queryset = Product.objects.all()         

  def destroy(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      instance.status = False
      instance.save()
    except Http404:
        pass
    return Response(status=status.HTTP_204_NO_CONTENT)  


class ParticipantView(viewsets.ModelViewSet):       
  """
  retrieve:
      Return the given Participant.

  list:
      Return a list of all Participants.

  create:
      Create a new Participant.

  destroy:
      Delete a Participant.

  update:
      Update a Participant.

  partial_update:
      Update a Participant.
  """   
  serializer_class = ParticipantSerializer          
  queryset = Participant.objects.all()    

  def destroy(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      instance.status = False
      instance.save()
    except Http404:
        pass
    return Response(status=status.HTTP_204_NO_CONTENT)  

class GameView(viewsets.ModelViewSet):       
  """
  retrieve:
      Return the given Game.

  list:
      Return a list of all Games.

  create:
      Create a new Game.

  destroy:
      Delete a Game.

  update:
      Update a Game.

  partial_update:
      Update a Game.
  """     
  serializer_class = GameSerializer          
  queryset = Game.objects.all()      

  def destroy(self, request, *args, **kwargs):
    try:
      instance = self.get_object()
      instance.status = False
      instance.save()
    except Http404:
        pass
    return Response(status=status.HTTP_204_NO_CONTENT)        