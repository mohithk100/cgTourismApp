from rest_framework import generics
from touristSpots.models import Places
from .serializers import PlaceSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

class List(generics.ListAPIView):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)