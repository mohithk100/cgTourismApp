from __future__ import unicode_literals
from django.db import models
import re


def get_upload_url(instance , filename):
    name = instance.name
    pattern = re.compile(r'\s+')
    name = re.sub(pattern, '', name)
    return 'Brochures/%s/%s'%( name , filename)

class Brochure(models.Model):
    name = models.CharField(max_length = 150)
    pdf = models.FileField(upload_to= get_upload_url)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Brochures'