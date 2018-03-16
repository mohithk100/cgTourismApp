from rest_framework import generics
from touristSpots.models import Places,PlaceReviews,Category
from .serializers import PlaceSerializer,ReviewSerializer,CategorySerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

class List(generics.ListAPIView):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer


class CreateReview(generics.CreateAPIView):
    queryset = PlaceReviews.objects.all()
    serializer_class = ReviewSerializer


class RetrievePlace(generics.ListAPIView):
    serializer_class = PlaceSerializer
    
    def get_queryset(self,**kwargs):
        category = self.kwargs['category']
        return Places.objects.filter(category__key = category)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MajorAttraction(generics.ListAPIView):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Places.objects.filter(major_attraction=True)