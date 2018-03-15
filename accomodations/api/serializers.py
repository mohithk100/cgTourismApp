from rest_framework import serializers
from accomodations.models import (
    CTB_Resorts,
    CTB_ResortImages,
    CTB_ResortFacilities,
    CTB_ResortTarrif,
    CTB_ResortOccupany,
    RegisteredHotels,
    RegisteredTravelOperators,
    CitywiseHotelList,
    TouristGuideList,
)


class MyPrimaryKeyRelatedFieldImage(serializers.PrimaryKeyRelatedField):
    def to_representation(self , value):
        return value.image.url


class MyPrimaryKeyRelatedFieldFacilities(serializers.PrimaryKeyRelatedField):
    def to_representation(self , value):
        return str(value.facility_name)


class MyPrimaryKeyRelatedFieldTarrif(serializers.PrimaryKeyRelatedField):
    def to_representation(self , value):
        print "THis ran"
        print value
        return {'checkin_time': value.checkin_time,'checkout_time': value.checkout_time}


class MyPrimaryKeyRelatedFieldOccupancy(serializers.PrimaryKeyRelatedField):
    def to_representation(self , value):
        return {'occupancy_type': value.occupancy_type,'occupancy_price': value.occupancy_price}


class CTB_ResortsSerializer(serializers.ModelSerializer):
    images = MyPrimaryKeyRelatedFieldImage(many = True , queryset = CTB_ResortImages.objects.all())
    facilities = MyPrimaryKeyRelatedFieldFacilities(many = True, queryset = CTB_ResortFacilities.objects.all())
    tarrif = MyPrimaryKeyRelatedFieldTarrif(queryset = CTB_ResortTarrif.objects.all())
    occupancy = MyPrimaryKeyRelatedFieldOccupancy(many = True , queryset = CTB_ResortOccupany.objects.all())
    class Meta:
        model = CTB_Resorts
        fields = (
            'title',
            'short_location',
            'location',
            'images',
            'facilities',
            'tarrif',
            'occupancy',
        )


class RegisteredHotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredHotels
        fields = (
            'name',
            'address',
            'contact_no',
            'email',
            'website',
        )


class RegisteredTravelOperatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredTravelOperators
        fields = (
            'name',
            'address',
            'contact_no',
            'email',
        )


class CitywiseHotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitywiseHotelList
        fields = (
            'city_name',
            'pdf',
        )


class TouristGuideListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristGuideList
        fields = (
            'name',
            'number',
            'district',
        )