from rest_framework import serializers
from downloads.models import (
    Brochure,
    Publication,
    RegisterationForm,
    CTB_Newsletter,
    ImportantDocument,
)


class BrochureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brochure
        fields = ('name','pdf')
        

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('name','pdf')


class RegisterationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterationForm
        fields = ('name','pdf')


class CTB_NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CTB_Newsletter
        fields = ('name','pdf')


class ImportantDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('name','pdf')