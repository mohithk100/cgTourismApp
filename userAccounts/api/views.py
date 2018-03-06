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
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsOwner,IsAdminUser)

class Create(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAdminUser,)
