from django.conf.urls import url,include
from .views import BrochureList

urlpatterns = [
    url(r'^brochure/list/$', BrochureList.as_view(), name = 'BrochureList'),
]