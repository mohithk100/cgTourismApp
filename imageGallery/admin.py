from __future__ import unicode_literals
from django.contrib import admin
from .models import ImageGallery

class ImageGalleryAdmin(admin.ModelAdmin):
    list_display=('name','image')

admin.site.register(ImageGallery, ImageGalleryAdmin)