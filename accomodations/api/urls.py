from django.conf.urls import url,include
from .views import (
    ResortsList,
    RegisteredHotelsList,
    TravelOperatorsList,
    CityWiseHotelList,
    TouristGuideList
)

urlpatterns = [
    url(r'^cbt_resorts/list/$', ResortsList.as_view() , name='CTBResortsList'),
    url(r'^registered_hotels/list/$', RegisteredHotelsList.as_view(), name = 'RegisteredHotelsList'),
    url(r'^registered_travel_operators/list/$', TravelOperatorsList.as_view(), name = 'TravelOperatorList'),
    url(r'^city_hotel/list/$', CityWiseHotelList.as_view(), name = 'CitywiseHotelList'),
    url(r'^tourist_guide/list/$', TouristGuideList.as_view(), name = 'TouristGuideList'),
]