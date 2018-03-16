from rest_framework import generics
from .serializers import (
    BrochureSerializer,
    PublicationSerializer,
    RegisterationFormSerializer,
    CTB_NewsletterSerializer,
    ImportantDocumentSerializer,
)
from downloads.models import (
    Brochure,
    Publication,
    RegisterationForm,
    CTB_Newsletter,
    ImportantDocument,
)


class BrochureList(generics.ListAPIView):
    queryset = Brochure.objects.all()
    serializer_class = BrochureSerializer

class PublicationList(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class RegisterationFormList(generics.ListAPIView):
    queryset = RegisterationForm.objects.all()
    serializer_class = RegisterationFormSerializer


class CTB_NewsletterList(generics.ListAPIView):
    queryset = CTB_Newsletter.objects.all()
    serializer_class = CTB_NewsletterSerializer

class ImportantDocumentList(generics.ListAPIView):
    queryset = ImportantDocument.objects.all()
    serializer_class = ImportantDocumentSerializer