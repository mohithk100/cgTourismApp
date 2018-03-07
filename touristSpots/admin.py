from __future__ import unicode_literals
from django.contrib import admin
from .models import Places,PlaceImages

class PlaceImagesInline(admin.TabularInline):
    model = PlaceImages
    extra = 3

class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImagesInline,]
    list_display = ('name', 'category' ,'major_attraction' )


admin.site.register(Places,PlaceAdmin)



