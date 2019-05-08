
# backend/urls.py

from django.contrib import admin
from django.urls import path, include                 # add this
from rest_framework import routers                    # add this
# from todo import views                            # add this
from gameBar import views

router = routers.DefaultRouter()                      # add this
# router.register(r'todos', views.TodoView, 'todo')     # add this
router.register(r'games', views.GameView, 'game')     # add this        
router.register(r'bar', views.BarView, 'bar')
router.register(r'participants', views.ParticipantView, 'participant')
router.register(r'products', views.ProductView, 'product')

urlpatterns = [
    path('admin/', admin.site.urls),           
    path('api/', include(router.urls))                # add this
]