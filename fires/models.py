from django.contrib.gis.db import models


class Satellite(models.Model):
    satellite = models.CharField('спутник', max_length=5, unique=True)
    short_satellite_name = models.CharField('спутник сокращенно', max_length=1, unique=True)

    class Meta:
        verbose_name = 'Спутник'
        verbose_name_plural = 'Спутники'
    
    def __str__(self):
        return str(self.satellite)


class Fire(models.Model):
    date = models.DateTimeField('дата и время (UTC) получения данных о MODIS')
    satellite = models.ForeignKey(Satellite)
    confidence = models.DecimalField('достоверность (0-100%)', max_digits=3, decimal_places=0)
    frp = models.DecimalField('мощность пожара', max_digits=5, decimal_places=1)
    brightness21 = models.DecimalField('температура по каналу 21/22 (в Кельвинах)', max_digits=4, decimal_places=1)
    brightness31 = models.DecimalField('температура по каналу 31 (в Кельвинах)', max_digits=4, decimal_places=1)
    scan = models.DecimalField('размер пиксела в направлении сканирования', max_digits=2, decimal_places=1)
    track = models.DecimalField('размер пиксела в направлении траектории', max_digits=2, decimal_places=1)
    version = models.DecimalField('версия', max_digits=2, decimal_places=1)
    geometry = models.PointField(srid=4326)
    objects = models.GeoManager()
    
    class Meta:
        unique_together = ('date', 'satellite', 'confidence', 'frp', 'brightness21', 'brightness31',
                           'scan', 'track', 'version', 'geometry')
        verbose_name = 'MODIS данные о пожаре'
        verbose_name_plural = 'MODIS данные о пожарах'
        
    def __str__(self):
        return str(self.date)
