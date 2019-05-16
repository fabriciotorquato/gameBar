
# todo/serializers.py

from rest_framework import serializers
from .models import Bar, Game, Participant, Product
      

class ParticipantSerializer(serializers.ModelSerializer):
  class Meta:
    model = Participant
    fields = ('id', 'name', 'status')

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('id', 'name', 'value','bar',  'status')

class GameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Game
    fields = ('id', 'title','product','bar', 'description' ,'participantA','participantB','winner', 'opened', 'closed')


class BarSerializer(serializers.ModelSerializer):
  products = ProductSerializer(many=True, read_only=True)
  games = GameSerializer(many=True, read_only=True)
  class Meta:
    model = Bar
    fields = ('id', 'name', 'description', 'address', 'products', 'games', 'status')
