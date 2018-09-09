from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import NotAcceptable, NotFound
from .serializers import TweetSerializer, UserSerializer, CommentSerializer, LikeSerializer
from .models import Tweet, Comment, Like
from .permissions import IsOwner
from .pagination import APIPagination
from django.contrib.auth.models import User
from django.db.models import Q


class ListPublicTweetsView(generics.ListAPIView):
    queryset = Tweet.objects.filter(is_public=True)
    serializer_class = TweetSerializer
    pagination_class = APIPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(Q(is_public=True) & Q(type=0))

        for tweet in queryset:
            tweet_id = tweet.id
            likes_count = Like.objects.filter(tweet=tweet_id).count()

            tweet.likes_count = likes_count
            tweet.comments_count = tweet.comments.all().count()
            tweet.save()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ListCreateTweetView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner)
    pagination_class = APIPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, type=0)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter((Q(owner=request.user) | Q(is_public=True)) & Q(type=0))

        for tweet in queryset:
            tweet_id = tweet.id
            likes_count = Like.objects.filter(tweet=tweet_id).count()

            tweet.likes_count = likes_count
            tweet.comments_count = tweet.comments.all().count()
            tweet.save()

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


class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner)
    pagination_class = APIPagination

    def perform_create(self, serializer):
        parent_id = int(self.request.data['parent'])
        tweets = Tweet.objects.filter(id=parent_id, is_public=True)

        if tweets.count() != 1:
            raise NotFound()

        serializer.save(owner=self.request.user, type=1, is_public=True, parent_id=parent_id)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter((Q(owner=request.user) | Q(is_public=True)) & Q(type=1))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ListUpdateDeleteCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner)
    pagination_class = APIPagination

    def perform_update(self, serializer):
        comment_id = int(self.kwargs.get('pk'))

        queryset = self.filter_queryset(self.queryset)
        queryset = queryset.filter(Q(id=comment_id) & Q(owner=self.request.user))

        if queryset.count() != 1:
            raise NotFound("Comment not found.")

        comment = queryset.get()

        serializer.save(parent=comment.parent, is_public=True)


class CreateDeleteLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner)
    pagination_class = APIPagination

    def perform_create(self, serializer):
        if self.request.data['author'] != str(self.request.user.id):
            raise NotAcceptable("Not authorized.")

        queryset = self.filter_queryset(self.get_queryset())
        subset = queryset.filter(Q(author_id=self.request.data['author']) & Q(tweet_id=self.request.data['tweet']))

        if subset.count() > 0:
            subset.first().delete()
            return

        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # queryset = queryset.filter(Q(author=request.user) | Q(is_public=True))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = APIPagination


class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = APIPagination
