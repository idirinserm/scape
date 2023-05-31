from django.contrib.gis.db import models
from jsonfield import JSONField
from rest_framework import serializers


class Shapefile(models.Model):
    type = models.CharField(max_length=50)
    geometry = models.GeometryField(srid=4326, null=True)
    properties = JSONField(default=dict)

    def set_property(self, key, value):
        """
        Sets a property on the `properties` JSONField.
        """
        self.properties[key] = value
        self.save()

    def get_properties_serializer(self):
        """
        Returns a dynamic serializer for the `properties` JSONField.
        """
        properties = self.properties or {}
        fields = {}
        for key in properties.keys():
            field = serializers.CharField()
            fields[key] = field
        return serializers.Serializer('DynamicPropertiesSerializer', fields=fields)


    def ObjectName(self):
        properties = self.properties or {}
        fields = {}
        nom = ""
        for key in properties.keys():
            properties[key] = nom
        return nom
