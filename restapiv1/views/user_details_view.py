from django.contrib.auth.models import User
from rest_framework import generics

from ..pagination import APIPagination
from ..serializers import UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = APIPagination
