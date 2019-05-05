
# todo/serializers.py

from rest_framework import serializers
from .models import GameBar
      
class GameBarSerializer(serializers.ModelSerializer):
  class Meta:
    model = GameBar
    fields = ('id', 'title', 'description', 'completed')