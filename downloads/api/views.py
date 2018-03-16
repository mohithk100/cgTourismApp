from rest_framework import generics
from .serializers import BrochureSerializer
from downloads.models import Brochure


class BrochureList(generics.ListAPIView):
    queryset = Brochure.objects.all()
    serializer_class = BrochureSerializer