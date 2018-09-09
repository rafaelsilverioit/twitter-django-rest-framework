from rest_framework import generics

from ..models import Tweet
from ..serializers import TweetSerializer
from ..utils import override_view_attributes


class ListUpdateDeleteTweetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        override_view_attributes(self)
