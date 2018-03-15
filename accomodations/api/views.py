from rest_framework import generics
from .serializers import (
    CTB_ResortsSerializer,
    RegisteredHotelsSerializer,
    RegisteredTravelOperatorsSerializer,
)
from accomodations.models import (
    CTB_Resorts,
    RegisteredHotels,
    RegisteredTravelOperators,
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

