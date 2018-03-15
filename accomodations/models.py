from __future__ import unicode_literals
from django.db import models
import re



def get_upload_url(instance , filename):
    name = instance.CTB_Resort.title
    pattern = re.compile(r'\s+')
    name = re.sub(pattern, '', name)
    return 'CTB_ResortImages/%s/%s'%( name , filename)


class CTB_Resorts(models.Model):
    title = models.CharField(max_length = 200)
    short_location = models.CharField(max_length = 20,blank = True)
    location = models.TextField(max_length= 150,blank=True)
    
    def __str__(self):
        return unicode(self.title)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name_plural = 'CTB_Resorts'


class CTB_ResortImages(models.Model):
    CTB_Resort = models.ForeignKey(CTB_Resorts , related_name='images',on_delete=models.SET_NULL,null = True)
    image = models.ImageField(upload_to = get_upload_url)

    def __str__(self):
        return unicode(self.CTB_Resort.title)

    def __unicode__(self):
        return unicode(self.CTB_Resort.title)

    class Meta:
        verbose_name_plural = 'CTB_ResortImages'


class CTB_ResortFacilities(models.Model):
    CTB_Resort = models.ForeignKey(CTB_Resorts, related_name='facilities', on_delete=models.SET_NULL, null = True)
    facility_name = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return unicode(self.CTB_Resort.title)

    def __unicode__(self):
        return unicode(self.CTB_Resort.title)

    class Meta:
        verbose_name_plural = 'CTB_ResortFacilities'


class CTB_ResortTarrif(models.Model):
    CTB_Resort = models.OneToOneField(CTB_Resorts,related_name='tarrif', on_delete=models.SET_NULL, null = True )
    checkin_time = models.CharField(max_length = 50 , blank = True)
    checkout_time = models.CharField(max_length = 50 , blank = True)

    def __str__(self):
        return unicode(self.CTB_Resort.title)

    def __unicode__(self):
        return unicode(self.CTB_Resort.title)

    class Meta:
        verbose_name_plural = 'CTB_ResortTarrif'


class CTB_ResortOccupany(models.Model):
    CTB_Resort = models.ForeignKey(CTB_Resorts, related_name='occupancy', on_delete=models.SET_NULL, null = True)
    occupancy_type = models.CharField(max_length= 500,blank = True)
    occupancy_price = models.CharField(max_length = 500, blank = True)

    def __str__(self):
        return unicode(self.CTB_Resort.title)

    def __unicode__(self):
        return unicode(self.CTB_Resort.title)

    class Meta:
        verbose_name_plural = 'CTB_ResortOccupany'


class RegisteredHotels(models.Model):
    name = models.CharField(max_length = 100)
    address = models.TextField(max_length=300,blank=True)
    contact_no = models.CharField(max_length=300,blank = True)
    email = models.EmailField(max_length = 254)
    website = models.URLField()

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Registered Hotels'


class RegisteredTravelOperators(models.Model):
    name = models.CharField(max_length = 250)
    address = models.CharField(max_length = 255)
    contact_no = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Registered Tour and Travel Operators'

