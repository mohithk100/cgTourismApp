from userAccounts.models import User
from .serializers import UserSerializer
from rest_framework import generics 
from .permissions import IsOwner
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

class Retrieve(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class Create(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
