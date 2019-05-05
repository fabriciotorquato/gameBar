
# todo/admin.py
    
from django.contrib import admin
from .models import GameBar # add this
    
class GameBarAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'completed') # add this
        
# Register your models here.
admin.site.register(GameBar, GameBarAdmin) # add this