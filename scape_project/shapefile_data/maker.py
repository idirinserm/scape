import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scape_project.settings")
import django
django.setup()

from shapefile_data.models import Shapefile
from osgeo import ogr
from django.contrib.gis.geos import GEOSGeometry

# define the SRS using osgeo.ogr
srs = ogr.osr.SpatialReference()
srs.ImportFromEPSG(2154)

# open the shapefile
shapefile_path = '/Users/idir/etna/scape/shapefiles_bank/Communes_d_%C3%8Ele-de-France__au_01_janvier_2019.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
dataset = driver.Open(shapefile_path, 0)
layer = dataset.GetLayer()

for feature in layer:
    geometry = feature.GetGeometryRef()
    # Check if the geometry has an SRS defined
    if geometry.GetSpatialReference() is None:
        # If not, set the SRS to the desired SRS
        geometry.AssignSpatialReference(srs)
    # Transform the geometry to the desired SRS
    geometry.TransformTo(srs)
    # Export the geometry to WKT in the transformed SRS
    wkt = geometry.ExportToWkt()
    # Create the Shapefile instance with the transformed geometry
    shapefile = Shapefile(geometry=GEOSGeometry(wkt, srid=4326))
    shapefile.save()