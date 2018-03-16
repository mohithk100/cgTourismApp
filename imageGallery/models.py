from __future__ import unicode_literals
from django.db import models

def get_upload_url(instance , filename):
    return 'ImageGallery/%s'%(filename)


class ImageGallery(models.Model):
    name = models.CharField(max_length = 100,)
    image = models.ImageField(upload_to = get_upload_url,blank = True)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural='ImageGallery'
