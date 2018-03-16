from imageGallery.models import ImageGallery
from rest_framework import serializers


class ImageGallerySerializer(serializers.ModelSerializer):
    class  Meta:
        model = ImageGallery
        fields = ('name','image')