from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import TweetSerializer, UserSerializer
from .models import Tweet
from .permissions import IsOwner
from .pagination import APIPagination
from django.contrib.auth.models import User
from django.db.models import Q


class ListTweetView(generics.ListAPIView):
    queryset = Tweet.objects.filter(is_public=True)
    serializer_class = TweetSerializer
    pagination_class = APIPagination


class ListCreateTweetView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner)
    pagination_class = APIPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(Q(owner=request.user) | Q(is_public=True))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ListUpdateDeleteTweetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner)
    pagination_class = APIPagination


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = APIPagination


class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = APIPagination
