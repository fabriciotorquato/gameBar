from django.contrib import admin
from .models import Bar, Participant, Product, Game
    
#class BarAdmin(admin.ModelAdmin):  # add this
#  list_display = ('title', 'description', 'completed') # add this
        
# Register your models here.
admin.site.register(Bar)
admin.site.register(Participant)
admin.site.register(Product)
admin.site.register(Game)