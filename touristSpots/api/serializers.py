from rest_framework import serializers
from touristSpots.models import Places,PlaceImages
from django.utils import six



class MyPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self , value):
        return value.image.url

class PlaceSerializer(serializers.ModelSerializer):
    images = MyPrimaryKeyRelatedField(many=True, queryset=PlaceImages.objects.all())
    class Meta:
        model = Places
        fields = (
            'name',
            'description',
            'major_attraction',
            'category',
            'location',
            'images',
            )
