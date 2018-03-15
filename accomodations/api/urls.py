from django.conf.urls import url,include
from .views import (
    ResortsList,
    RegisteredHotelsList,
    TravelOperatorsList,
)

urlpatterns = [
    url(r'^cbt_resorts/list/$', ResortsList.as_view() , name='CTBResortsList'),
    url(r'^registered_hotels/list/$', RegisteredHotelsList.as_view(), name = 'RegisteredHotelsList'),
    url(r'^registered_travel_operators/list/$', TravelOperatorsList.as_view(), name = 'TravelOperatorList'),
]