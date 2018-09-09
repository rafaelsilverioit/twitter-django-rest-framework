from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Tweet
        fields = ('id', 'text', 'owner', 'is_public', 'created_at', 'modified_at')
        read_only_fields = ('created_at', 'modified_at')


class UserSerializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tweet.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'tweets')
