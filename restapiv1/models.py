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
    is_public = models.BooleanField(default=False, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
