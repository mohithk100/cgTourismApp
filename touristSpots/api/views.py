from rest_framework import generics
from touristSpots.models import Places,PlaceReviews
from .serializers import PlaceSerializer,ReviewSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

class List(generics.ListAPIView):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)


class CreateReview(generics.CreateAPIView):
    queryset = PlaceReviews.objects.all()
    serializer_class = ReviewSerializer
    authentication_class = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
