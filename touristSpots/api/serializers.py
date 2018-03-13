from rest_framework import serializers
from touristSpots.models import Places,PlaceImages,PlaceReviews
from django.utils import six



class MyPrimaryKeyRelatedFieldImage(serializers.PrimaryKeyRelatedField):
    def to_representation(self , value):
        return value.image.url

class MyPrimaryKeyRelatedFieldPlace(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return {value.user.username:value.review,}

class PlaceSerializer(serializers.ModelSerializer):
    images = MyPrimaryKeyRelatedFieldImage(many=True, queryset=PlaceImages.objects.all())
    reviews_place = MyPrimaryKeyRelatedFieldPlace(many=True, queryset=PlaceReviews.objects.all())
    class Meta:
        model = Places
        fields = (
            'name',
            'description',
            'major_attraction',
            'category',
            'location',
            'images',
            # 'reviews_user',
            'reviews_place',
            )
