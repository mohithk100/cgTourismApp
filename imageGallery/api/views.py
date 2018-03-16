from rest_framework import generics
from .serializers import ImageGallerySerializer
from imageGallery.models import ImageGallery


class ImageGallery(generics.ListAPIView):
    queryset = ImageGallery.objects.all()
    serializer_class = ImageGallerySerializer