from __future__ import unicode_literals
from django.contrib import admin
from .models import (
    Brochure,
    Publication,
    RegisterationForm,
    CTB_Newsletter,
    ImportantDocument,
)


class BrochureAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PublicationAdmin(admin.ModelAdmin):
    list_display=('name',)

class RegisterationFormAdmin(admin.ModelAdmin):
    list_display=('name',)

class CTB_NewsletterAdmin(admin.ModelAdmin):
    list_display=('name',)

class ImportantDocumentAdmin(admin.ModelAdmin):
    list_display=('name',)


admin.site.register(Brochure,BrochureAdmin)
admin.site.register(Publication,PublicationAdmin)
admin.site.register(RegisterationForm,RegisterationFormAdmin)
admin.site.register(CTB_Newsletter,CTB_NewsletterAdmin)
admin.site.register(ImportantDocument,ImportantDocumentAdmin)
