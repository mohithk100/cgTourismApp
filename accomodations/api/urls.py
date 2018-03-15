from django.conf.urls import url,include
from .views import ResortsList

urlpatterns = [
    url(r'^list/$', ResortsList.as_view() , name='CTBResortsList'),
]