from rest_framework import serializers
from touristSpots.models import Places,PlaceImages,PlaceReviews,Category
from django.utils import six
from userAccounts.models import User



class MyPrimaryKeyRelatedFieldImage(serializers.PrimaryKeyRelatedField):
    def to_representation(self , value):
        return value.image.url

class MyPrimaryKeyRelatedFieldPlace(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return {'username':value.user.username,'review':value.review,'avatar':value.user.avatar.url,}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
            'key',
            'description',
            'image',
        )

class PlaceSerializer(serializers.ModelSerializer):
    images = MyPrimaryKeyRelatedFieldImage(many=True, queryset=PlaceImages.objects.all())
    reviews_place = MyPrimaryKeyRelatedFieldPlace(many=True, queryset=PlaceReviews.objects.all())
    class Meta:
        model = Places
        fields = (
            'name',
            'description',
            'major_attraction',
            'location',
            'latitude',
            'longitude',
            'images',
            'reviews_place',
            )


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 50)
    placename = serializers.CharField(max_length = 100)
    success = serializers.BooleanField(default = False)
    class Meta:
        model = PlaceReviews
        fields = (
            'username',
            'placename',
            'review',
            'success',
        )
        extra_kwargs={
            'username':{
                'write_only':True,
            },
            'placename':{
                'write_only':True,
            },
            'success':{
                'write_only':True,
            }
        } 

    def create(self,validated_data):
        try:
            username = validated_data['username']
            placename = validated_data['placename']
            review = validated_data['review']
            user_model = User.objects.filter(username = username)
            place_model = Places.objects.get(name = placename)
            review = PlaceReviews(
                review = review,
            )
            review.user_id = user_model.values('id')[0]['id']
            review.place_id = place_model.id
            review.save()
            validated_data['success'] = True
            print validated_data
            return validated_data
        except:
            validated_data['success'] = False
            return validated_data


