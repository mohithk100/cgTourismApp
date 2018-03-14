from __future__ import unicode_literals
from decimal import Decimal
from django.db import models
from userAccounts.models import User
import re


def get_upload_url(instance , filename):
    name = instance.place.name
    pattern = re.compile(r'\s+')
    name = re.sub(pattern, '', name)
    return 'touristSpotsImages/%s/%s'%( name , filename)

def get_category_upload_url(instance, filename):
    name = instance.title
    pattern = re.compile(r'\s+')
    name = re.sub(pattern , '' ,name)
    return 'CategoryImages/%s/%s'%(name , filename)

class Category(models.Model):
    key = models.CharField(max_length = 60,unique = True)
    title = models.CharField(max_length = 80, unique = True)
    description = models.TextField(max_length=1000,blank= True)
    image = models.ImageField(upload_to =get_category_upload_url , default = 'CategoryImages/defaultImage/defaultCategoryImage.jpg')

    def __str__(self):
        return unicode(self.title)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name_plural='Categories'


class Places(models.Model):
    name = models.CharField(max_length = 255 , blank = False)
    description = models.TextField(max_length = 2500,blank = True)
    major_attraction = models.BooleanField(default = False)
    location = models.CharField(max_length = 255,blank = True)
    latitude = models.DecimalField(blank = True,max_digits=9,decimal_places=6,default = Decimal('0.0000'))
    longitude =models.DecimalField(blank = True,max_digits=9,decimal_places=6,default = Decimal('0.0000'))
    category = models.ForeignKey(Category,related_name='category',on_delete=models.SET_NULL,null = True)

    def ___str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Places"


class PlaceImages(models.Model):
    place = models.ForeignKey(Places, related_name = 'images')
    image = models.ImageField(upload_to=get_upload_url)

    def ___str__(self):
        return self.place.name

    def __unicode__(self):
        return unicode(self.image.url)

    class Meta:
        verbose_name_plural="Images"


class PlaceReviews(models.Model):
    user = models.ForeignKey(User, related_name='reviews_user',on_delete=models.SET_NULL,null=True)
    place = models.ForeignKey(Places, related_name='reviews_place',on_delete=models.SET_NULL , null = True)
    review = models.TextField(max_length=500)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return unicode(self.user.username)

    class Meta:
        verbose_name_plural="PlaceReviews"





    
