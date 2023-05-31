import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scape_project.settings")
import django
django.setup()
from django.contrib.gis.geos import GEOSGeometry
from osgeo import ogr


def import_shapefile(shapefile_path):
    # Open the shapefile
    shapefile = ogr.Open(shapefile_path)
    layer = shapefile.GetLayer()

    # Convert the "geometry" field to WKT format and store the data in a list of dictionaries
    features = []
    for feature in layer:
        geometry = feature.GetGeometryRef()
        wkt = geometry.ExportToWkt()
        properties = {}
        for i in range(feature.GetFieldCount()):
            field_name = feature.GetFieldDefnRef(i).GetName()
            field_value = feature.GetField(i)
            properties[field_name] = field_value
        features.append({
            'geometry': wkt,
            'properties': properties
        })

    # Create a Shapefile object for each feature and save it to the database
    for feature in features:
        shapefile = Shapefile(
            geometry=GEOSGeometry(feature['geometry']),
            properties=feature['properties']
        )
        shapefile.save()


if __name__ == '__main__':
    # Import the Shapefile model
    from shapefile_data.models import Shapefile

    # Call the import_shapefile function with the path to your shapefile
    shapefile_path = '/Users/idir/etna/scape/shapefiles_bank/Communes_d_%C3%8Ele-de-France__au_01_janvier_2019.shp'
    import_shapefile(shapefile_path)
