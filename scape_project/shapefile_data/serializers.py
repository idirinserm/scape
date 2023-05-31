from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from shapefile_data.models import Shapefile


class ShapefilePropertiesSerializer(serializers.Serializer):
    """
    A serializer for the `properties` JSONField.
    """
    def to_representation(self, instance):
        """
        Override the default method to dynamically generate fields for the JSONField.
        """
        data = {}
        for key, value in instance.items():
            data[key] = value
        return data

    def to_internal_value(self, data):
        """
        Override the default method to validate the input data for the JSONField.
        """
        if not isinstance(data, dict):
            raise serializers.ValidationError('Invalid input data')
        return {'properties': data}


class ShapefileSerializer(GeoFeatureModelSerializer):
    """
    A serializer for the Shapefile model.
    """
    properties = serializers.JSONField()

    class Meta:
        fields = ['properties', 'geometry']
        model = Shapefile
        geo_field = 'geometry'

    def update(self, instance, validated_data):
        """
        Override the default method to update the `properties` JSONField.
        """
        properties_data = validated_data.pop('properties', None)
        if properties_data is not None:
            for key, value in properties_data.items():
                instance.set_property(key, value)
        return super().update(instance, validated_data)
