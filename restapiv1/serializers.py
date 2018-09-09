from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tweet, Comment, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'author', 'tweet')


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'owner', 'is_public', 'type', 'likes_count', 'comments_count', 'comments', 'parent',
                  'created_at', 'modified_at')

    def get_fields(self):
        fields = super(CommentSerializer, self).get_fields()
        fields['comments'] = CommentSerializer(many=True, read_only=True)

        return fields


class TweetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Tweet
        fields = ('id', 'text', 'owner', 'is_public', 'type', 'likes_count', 'comments_count', 'comments', 'created_at',
                  'modified_at')
        read_only_fields = ('created_at', 'modified_at')


class UserSerializer(serializers.ModelSerializer):
    tweets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tweet.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'tweets')
