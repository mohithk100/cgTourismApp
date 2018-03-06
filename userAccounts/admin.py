from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class customUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None , {'fields':('mobileNumber','country','avatar','description',)}),
    )
    list_display = ('username','email','mobileNumber','country','is_staff')

admin.site.register(User , customUserAdmin)