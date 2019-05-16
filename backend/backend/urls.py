from django.contrib import admin
from django.urls import path, include    
from rest_framework import routers                    
from rest_framework.schemas import get_schema_view
from rest_framework_swagger import renderers
from django.conf.urls import url
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from gameBar import views


schema_view = get_schema_view(
    title='Swagger documentation',
    renderer_classes = [OpenAPIRenderer, SwaggerUIRenderer],
)

router = routers.DefaultRouter()    

router.register(r'games', views.GameView, 'game')             
router.register(r'bars', views.BarView, 'bar')
router.register(r'participants', views.ParticipantView, 'participant')
router.register(r'products', views.ProductView, 'product')

urlpatterns = [
    url('admin/', admin.site.urls),  
    url('api/', include(router.urls))  ,
    url('docs/', schema_view),               
]