
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
    fields = ('id', 'name', 'value', 'status')

class GameSerializer(serializers.ModelSerializer):
  participantA = ParticipantSerializer(read_only=True)
  participantB = ParticipantSerializer(read_only=True)
  winner = ParticipantSerializer(read_only=True)
  class Meta:
    model = Game
    fields = ('id', 'title', 'description' ,'participantA','participantB','winner', 'opened', 'closed')


class BarSerializer(serializers.ModelSerializer):
  products = ProductSerializer(many=True, read_only=True)
  games = GameSerializer(many=True, read_only=True)
  class Meta:
    model = Bar
    fields = ('id', 'name', 'description', 'address', 'products', 'games', 'status')
