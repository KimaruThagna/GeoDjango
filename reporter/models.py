from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.db.models.signals import pre_save
from django.dispatch import receiver
import geocoder
# Create your models here.
status={
    ('1',"BAD"),('2',"MODERATE"),('3',"WORSE"),
}
class Incidence(models.Model):
    name=models.CharField(max_length=20)
    status = models.CharField(max_length=50,choices=status )
    nature=models.CharField(max_length=50)
    description=models.CharField(max_length=200,default='The above problem')
    location=models.PointField(null=True,srid=4326,blank=True) #srid....spatial reference ID
    objects=models.GeoManager()

    def __str__(self):
        return self.nature


# run python3 manage.py ogrinspect /path/to/shp datafile 'give model name' --srid=4326 --mapping(this creates a model) --multi(use multiple items to create model)

class Counties(models.Model):
    class Meta:
        verbose_name_plural = 'Counties'
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.counties

@receiver(pre_save,sender=Incidence)

def loc_assign(sender, instance, *args, **kwargs):
   geocode= geocoder.google(str(instance.name))
   latitude=geocode.latlng[0]
   longitude=geocode.latlng[1]
   point = GEOSGeometry('POINT(%s %s)' % (longitude,latitude ))
   instance.location=point


pre_save.connect(loc_assign,sender=Incidence)

