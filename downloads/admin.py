from __future__ import unicode_literals
from django.contrib import admin
from .models import Brochure


class BrochureAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Brochure,BrochureAdmin)
