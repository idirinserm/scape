from rest_framework import mixins, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny

from commune.models import Commune
from commune.serializers import CommuneSerializer


class CommuneViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]
