from __future__ import unicode_literals
from django.contrib import admin
from .models import (
    CTB_Resorts,
    CTB_ResortImages,
    CTB_ResortFacilities,
    CTB_ResortTarrif,
    CTB_ResortOccupany,
    RegisteredHotels,
    RegisteredTravelOperators,
    CitywiseHotelList,
    TouristGuideList,
)

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


class RegisteredHotelsAdmin(admin.ModelAdmin):
    list_display= ('name','email','contact_no',)


class RegisteredTravelOperatorsAdmin(admin.ModelAdmin):
    list_display = ('name','contact_no','email')


class TouristGuideListAdmin(admin.ModelAdmin):
    list_display = ('name','number','district')


admin.site.register(CTB_Resorts,CTB_ResortsAdmin)
admin.site.register(RegisteredHotels,RegisteredHotelsAdmin)
admin.site.register(RegisteredTravelOperators,RegisteredHotelsAdmin)
admin.site.register(CitywiseHotelList)
admin.site.register(TouristGuideList,TouristGuideListAdmin)

