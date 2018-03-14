from rest_framework import generics
from touristSpots.models import Places,PlaceReviews,Category
from .serializers import PlaceSerializer,ReviewSerializer,CategorySerializer
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


class RetrievePlace(generics.ListAPIView):
    serializer_class = PlaceSerializer
    
    def get_queryset(self,**kwargs):
        category = self.kwargs['category']
        return Places.objects.filter(category__key = category)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer