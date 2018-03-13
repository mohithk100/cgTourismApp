from django.conf.urls import url,include
from .views import List,CreateReview

urlpatterns = [
    url(r'^list/$',List.as_view(),name='placesListApiView'),
    url(r'^review/add/$',CreateReview.as_view(),name = 'reviewCreateApiView'),
]