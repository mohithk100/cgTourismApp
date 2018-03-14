from __future__ import unicode_literals
from django.contrib import admin
from .models import Places,PlaceImages,PlaceReviews,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('key', 'title')


class PlaceImagesInline(admin.TabularInline):
    model = PlaceImages
    extra = 3

class PlaceReviewsInline(admin.TabularInline):
    model = PlaceReviews
    extra = 3

class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImagesInline,PlaceReviewsInline]
    list_display = ('name', 'category' ,'major_attraction' )


admin.site.register(Places,PlaceAdmin)
admin.site.register(Category,CategoryAdmin)



