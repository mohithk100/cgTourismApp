from django.conf.urls import url,include
from .views import List

urlpatterns = [
    url(r'^list/$',List.as_view(),name='placesListApiView'),
]