from django.conf.urls import url,include
from .views import ImageGallery

urlpatterns = [
    url(r'^list/$', ImageGallery.as_view(), name = 'imageGallery'),
]