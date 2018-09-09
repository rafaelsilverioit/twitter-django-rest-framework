from django.db.models import Q
from rest_framework import generics
from rest_framework.exceptions import NotAcceptable

from ..models import Like
from ..serializers import LikeSerializer
from ..utils import override_view_attributes


class CreateDeleteLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        override_view_attributes(self)

    def perform_create(self, serializer):
        if self.request.data['author'] != str(self.request.user.id):
            raise NotAcceptable("Not authorized.")

        queryset = self.filter_queryset(self.get_queryset())
        subset = queryset.filter(Q(author_id=self.request.data['author']) & Q(tweet_id=self.request.data['tweet']))

        # If it's already liked, then just dislike.
        if subset.count() > 0:
            subset.first().delete()
            return

        serializer.save()
