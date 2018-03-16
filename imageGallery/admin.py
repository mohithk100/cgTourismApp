from __future__ import unicode_literals
from django.contrib import admin
from .models import ImageGallery,Images


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 3

class ImageGalleryAdmin(admin.ModelAdmin):
    inlines = [ImagesInline,]
    list_display=('name','image')

admin.site.register(ImageGallery, ImageGalleryAdmin)