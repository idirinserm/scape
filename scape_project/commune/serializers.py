from commune.models import Commune
from rest_framework_gis import serializers


class CommuneSerializer(serializers.GeoFeatureModelSerializer):

    class Meta:
        fields = ['nom', 'id', 'insee']
        model = Commune
        geo_field = 'geom'