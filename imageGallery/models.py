from __future__ import unicode_literals
from django.db import models

def get_upload_url(instance , filename):
    return 'ImageGallery/%s'%(filename)

def get_img_upload_url(instance , filename):
    return 'Images/%s'%()


class ImageGallery(models.Model):
    name = models.CharField(max_length = 100,)
    image = models.ImageField(upload_to = get_upload_url,blank = True)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural='ImageGallery'


class Images(models.Model):
    category = models.ForeignKey(ImageGallery,related_name='images_array',on_delete=models.SET_NULL,null = True)
    image =     image = models.ImageField(upload_to = get_upload_url,blank = True)

    def __str__(self):
        return unicode(self.category.name)

    def __unicode__(self):
        return unicode(self.category.name)

    class Meta:
        verbose_name_plural='Images'
