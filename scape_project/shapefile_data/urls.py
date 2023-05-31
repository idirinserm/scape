from django.urls import path, include
from rest_framework import routers

from shapefile_data.views import ShapefileViewSet

router = routers.DefaultRouter()
router.register(r'shapefile_data', ShapefileViewSet)

appname = 'shapefile'

urlpatterns = [
    path('', include(router.urls))
]
