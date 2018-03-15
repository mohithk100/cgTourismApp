from __future__ import unicode_literals
from django.contrib import admin
from .models import CTB_Resorts,CTB_ResortImages,CTB_ResortFacilities,CTB_ResortTarrif,CTB_ResortOccupany

class CTB_ResortOccupanyInline(admin.TabularInline):
    model = CTB_ResortOccupany
    extra = 3

class CTB_ResortTarrifInline(admin.StackedInline):
    model = CTB_ResortTarrif


class CTB_ResortImagesInline(admin.TabularInline):
    model = CTB_ResortImages
    extra = 2

class CTB_ResortFacilitiesInline(admin.TabularInline):
    model = CTB_ResortFacilities
    extra = 4

class CTB_ResortsAdmin(admin.ModelAdmin):
    inlines = [CTB_ResortImagesInline,CTB_ResortFacilitiesInline,CTB_ResortTarrifInline,CTB_ResortOccupanyInline]
    list_display = ('title','short_location',)

admin.site.register(CTB_Resorts,CTB_ResortsAdmin)



