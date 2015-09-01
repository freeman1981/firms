from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.gdal import DataSource
from django.db import IntegrityError

from datetime import datetime
from decimal import Decimal
import urllib.request
import zipfile
import os
import shutil

from fires.models import Fire, Satellite


def feature_to_model(feature):
    acq_datetime = ''.join([str(feature['ACQ_DATE']),
                            str(feature['ACQ_TIME'])])
    dt = datetime.strptime(acq_datetime, '%Y-%m-%d%H%M')
    data = {
        'date': dt,
        'satellite': Satellite.objects.get(short_satellite_name=str(feature['SATELLITE'])),
        'confidence': Decimal(str(feature['CONFIDENCE'])),
        'frp': Decimal(str(feature['FRP'])),
        'brightness21': Decimal(str(feature['BRIGHTNESS'])),
        'brightness31': Decimal(str(feature['BRIGHT_T31'])),
        'scan': Decimal(str(feature['SCAN'])),
        'track': Decimal(str(feature['TRACK'])),
        'version': Decimal(str(feature['VERSION'])),
        'geometry': feature.geom.geos
    }
    return Fire(**data)


class Command(BaseCommand):

    def handle(self, *args, **options):
        # TODO must be more clever solution!
        # url = ('/vsizip/vsicurl/'
        #        'https://firms.modaps.eosdis.nasa.gov/active_fire/shapes/zips/Global_24h.zip')
        urllib.request.urlretrieve('https://firms.modaps.eosdis.nasa.gov/active_fire/shapes/zips/Global_24h.zip',
                                   '/tmp/Global_24h.zip')
        zip_ = zipfile.ZipFile('/tmp/Global_24h.zip')
        zip_.extractall('/tmp/Global_24h')
        path = '/tmp/Global_24h/Global_24h.shp'
        ds = DataSource(path)
        layer = ds[0]
        for feature in layer:
            try:
                feature_to_model(feature).save()
            except IntegrityError:
                pass
        os.remove('/tmp/Global_24h.zip')
        shutil.rmtree('/tmp/Global_24h')
