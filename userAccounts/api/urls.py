from django.conf.urls import url,include 
from .views import (Retrieve,Create)

urlpatterns = [
    url(r'^retrieve/(?P<username>[.\w-]+)/$', Retrieve.as_view() , name ='UserRetrieveApiView'),
    url(r'^create/$',Create.as_view(),name='UserCreateApiView'),
]