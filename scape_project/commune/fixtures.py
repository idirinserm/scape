import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scape_project.settings")
import django
django.setup()
from django.contrib.gis.utils import LayerMapping

from commune.models import Commune

commune_mapping = {
    'insee': 'insee',
    'nom': 'nom',
    'part75_plus': 'part75+',
    'evo75_plus': 'evo75+',
    'parretrait': 'parretrait',
    'evo65seuls': 'evo65seuls',
    'mediane': 'mediane',
    'mediane75': 'mediane75',
    'partT5': 'partT5',
    'partmaison': 'partmaison',
    'a60ascenseu': '60ascenseu',
    'popasdense': 'popasdense',
    'partT5rp': 'partT5rp',
    'diffrevenu': 'diffrevenu',
    'cadres55an': 'cadres55an',
    's15_19seuls': '15-19seuls',
    's20_24seuls': '20-24seuls',
    't1529total': '1529total',
    'part1524se': 'part1524se',
    'atlasnb': 'atlasnb',
    'placetud': 'placetud',
    'densitplac': 'densitplac',
    'evojeunes': 'evojeunes',
    'T1T2': 'T1T2',
    'locataires': 'locataires',
    'geom': 'POLYGON',
}

def run(shapefile):
    layer_mapping = LayerMapping(
        Commune,
        shapefile,
        commune_mapping,
        transform=False,
        encoding='iso-8859-1',
    )
    layer_mapping.save(strict=True, verbose=True)



shapefile = os.path.abspath(os.path.join('/Users/idir/etna/shapefileCL', 'communes-2022_precis.shp'))
run(shapefile)
