from __future__ import unicode_literals
from django.db import models
import re


CHOICES = (
    ('cave','Cave'),
    ('dam','Dam'),
    ('hill','Hill'),
    ('monument','Monument'),
    ('museum','Museum'),
    ('national_park_and_bioshphere_reserve','National Park & Biosphere Reserve'),
    ('religious_attraction','Religious Attraction'),
    ('tiger_reserve','Tiger Reserve'),
    ('waterfall','Waterfall'),
    ('wildfile_sanctuary','Wildlife Sanctuary'),
    ('other','Other'),
)

def get_upload_url(instance , filename):
    name = instance.place.name
    pattern = re.compile(r'\s+')
    name = re.sub(pattern, '', name)
    return 'touristSpotsImages/%s/%s'%( name , filename)


class Places(models.Model):
    name = models.CharField(max_length = 255 , blank = False)
    description = models.TextField(max_length = 2500,blank = True)
    major_attraction = models.BooleanField(default = False)
    category = models.CharField(max_length = 255 , choices = CHOICES , blank = True)
    location = models.CharField(max_length = 255,blank = True)

    def ___str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Places"


class PlaceImages(models.Model):
    place = models.ForeignKey(Places , related_name = 'images')
    image = models.ImageField(upload_to=get_upload_url)

    def ___str__(self):
        return self.place.name

    class Meta:
        verbose_name_plural="Images"
