from django.urls import path, include
from rest_framework import routers

from commune.views import CommuneViewSet

router = routers.DefaultRouter()
router.register(r'commune', CommuneViewSet)

appname = 'commune'

urlpatterns = [
    path('', include(router.urls))
]
