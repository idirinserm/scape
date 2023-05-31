from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from shapefile_data.models import Shapefile
from shapefile_data.serializers import ShapefileSerializer


class ShapefileViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    queryset = Shapefile.objects.all()
    serializer_class = ShapefileSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]


