from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Tweet(models.Model):
    text = models.CharField(max_length=128, null=False, blank=False)
    owner = models.ForeignKey('auth.User',
                              related_name='tweets',
                              on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    type = models.IntegerField(default=0, null=False, blank=False, editable=False)
    likes_count = models.IntegerField(default=0, null=False, blank=False, editable=False)
    comments_count = models.IntegerField(default=0, null=False, blank=False, editable=False)

    def __str__(self):
        return self.text


class Like(models.Model):
    tweet = models.ForeignKey('Tweet',
                              related_name='like',
                              on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User',
                               related_name='author',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet.text


class Comment(Tweet):
    parent = models.ForeignKey('Tweet',
                               related_name='comments',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.text


# TODO: Instead of creating a token upon user creation, move it to a class which will be responsible for
# TODO: user account management and tokens will be generated upon user request, so the API access is limited.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
