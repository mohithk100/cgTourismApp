from .serializers import CTB_ResortsSerializer
from accomodations.models import CTB_Resorts
from rest_framework import generics


class ResortsList(generics.ListAPIView):
    queryset = CTB_Resorts.objects.all()
    serializer_class = CTB_ResortsSerializer

