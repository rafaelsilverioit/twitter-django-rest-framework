from rest_framework import generics
from rest_framework.exceptions import NotFound

from ..models import Tweet, Comment
from ..serializers import CommentSerializer
from ..utils import override_view_attributes


class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        override_view_attributes(self)

    def perform_create(self, serializer):
        parent_id = int(self.request.data['parent'])
        tweets = Tweet.objects.filter(id=parent_id, is_public=True)

        if tweets.count() != 1:
            raise NotFound()

        serializer.save(owner=self.request.user, type=1, is_public=True, parent_id=parent_id)
