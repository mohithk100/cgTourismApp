from __future__ import unicode_literals
from django.db import models
import re


def get_upload_url(instance , filename):
    name = instance.name
    pattern = re.compile(r'\s+')
    name = re.sub(pattern, '', name)
    return 'Brochures/%s/%s'%( name , filename)


def get_publications_upload_url(instance , filename):
    name = instance.name
    pattern = re.compile(r'\s+')
    name = re.sub(pattern, '', name)
    return 'Publications/%s/%s'%( name , filename)


def get_rf_upload_url(instance , filename):
    name = instance.name
    pattern = re.compile(r'\s+')
    name = re.sub(pattern, '', name)
    return 'RegisterationFrom/%s/%s'%( name , filename)


def get_ctb_upload_url(instance , filename):
    name = instance.name
    pattern = re.compile(r'\s+')
    name = re.sub(pattern, '', name)
    return 'CTB_Newsletter/%s/%s'%( name , filename)


def get_id_upload_url(instance , filename):
    name = instance.name
    pattern = re.compile(r'\s+')
    name = re.sub(pattern, '', name)
    return 'ImportantDocuments/%s/%s'%( name , filename)


class Brochure(models.Model):
    name = models.CharField(max_length = 150)
    pdf = models.FileField(upload_to= get_upload_url)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Brochures'


class Publication(models.Model):
    name = models.CharField(max_length = 150)
    pdf = models.FileField(upload_to= get_publications_upload_url)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Publications'


class RegisterationForm(models.Model):
    name = models.CharField(max_length = 150)
    pdf = models.FileField(upload_to= get_rf_upload_url)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Registeration Forms'

    
class CTB_Newsletter(models.Model):
    name = models.CharField(max_length = 150)
    pdf = models.FileField(upload_to= get_ctb_upload_url)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'CTB_NewsLetters'


class ImportantDocument(models.Model):
    name = models.CharField(max_length = 150)
    pdf = models.FileField(upload_to= get_id_upload_url)

    def __str__(self):
        return unicode(self.name)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Important Documents'


