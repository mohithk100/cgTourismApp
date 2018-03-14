from django.conf.urls import url,include
from .views import List,CreateReview,RetrievePlace,CategoryList

urlpatterns = [
    url(r'^list/$',List.as_view(),name='placesListApiView'),
    url(r'^review/add/$',CreateReview.as_view(),name = 'reviewCreateApiView'),
    url(r'^list/(?P<category>[.\w-]+)/$', RetrievePlace.as_view(), name= 'RetrieveAPIViewCategory'),
    url(r'category/list/$',CategoryList.as_view(),name='CategoryList'),
]