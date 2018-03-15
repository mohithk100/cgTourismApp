from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer,JSONRenderer
from rest_framework.response import Response
from .serializers import (
    CTB_ResortsSerializer,
    RegisteredHotelsSerializer,
    RegisteredTravelOperatorsSerializer,
    CitywiseHotelListSerializer,
    TouristGuideListSerializer,
)
from accomodations.models import (
    CTB_Resorts,
    RegisteredHotels,
    RegisteredTravelOperators,
    CitywiseHotelList,
    TouristGuideList,
)



class ResortsList(generics.ListAPIView):
    queryset = CTB_Resorts.objects.all()
    serializer_class = CTB_ResortsSerializer

class RegisteredHotelsList(generics.ListAPIView):
    queryset = RegisteredHotels.objects.all()
    serializer_class = RegisteredHotelsSerializer

class TravelOperatorsList(generics.ListAPIView):
    queryset = RegisteredTravelOperators.objects.all()
    serializer_class = RegisteredTravelOperatorsSerializer


class CityWiseHotelList(generics.ListAPIView):
    queryset = CitywiseHotelList.objects.all()
    serializer_class = CitywiseHotelListSerializer


class TouristGuideList(generics.ListAPIView):
    queryset = TouristGuideList.objects.all()
    serializer_class = TouristGuideListSerializer

class DiscountPolicy(APIView):

    renderer_classes = (JSONRenderer, )

    def get(self, request):
        data = {'pdf':reverse('/media/DiscountPolicy/discount.pdf') }
        return Response(data)