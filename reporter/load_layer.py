
import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

countie_mapping = {
    'counties' : 'Counties',
    'codes' : 'Codes',
    'cty_code' : 'Cty_CODE',
    'dis' : 'dis',
    'geom' : 'MULTIPOLYGON',
}

county_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/counties.shp'))
#the function loads data from the shp file into the model
def run(verbose=True):
    # give model,actual data,mapping dictionary,
	lm = LayerMapping(Counties, county_shp, countie_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose) # strict matches all fields exactly