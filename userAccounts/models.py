from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils.encoding import python_2_unicode_compatible


def get_upload_url(instance, filename):
    return 'userProfileImages/%s/%s'%(instance.username , filename)

@python_2_unicode_compatible
class User(AbstractUser):
    mobileNumber = PhoneNumberField(unique = True)
    country = CountryField(default = 'IN')
    avatar = models.ImageField(upload_to = get_upload_url, default = 'userProfileImages/default/defaultProfileImage.png' )
    description = models.CharField(max_length = 250 , blank = True)

    def __str__(self):
        return self.username



