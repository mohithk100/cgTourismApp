from rest_framework import serializers
from downloads.models import Brochure


class BrochureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brochure
        fields = ('name','pdf')
        