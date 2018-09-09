from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Tweet


def create_tweet(text, owner, is_public=False):
    return Tweet.objects.create(text=text, owner=owner, is_public=is_public)


class TweetTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='mars')

    def test_can_create_tweet(self):
        before = Tweet.objects.count()
        create_tweet('Hello World!', owner=self.user, is_public=False)

        after = Tweet.objects.count()

        self.assertNotEqual(before, after)

    def test_can_list_tweet(self):
        create_tweet('Hello World!', owner=self.user,  is_public=False)
        tweet = Tweet.objects.get()

        self.assertEquals(tweet.__str__(), 'Hello World!')


class ViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='mars')

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.tweet_data = {
            'text': 'Hello World!',
            'is_public': True,
            'type': 0
        }

        self.response = self.client.post(
            reverse('api:create'),
            self.tweet_data,
            format='json'
        )

    def test_api_can_create_tweet(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        n_client = APIClient()

        response = n_client.get(reverse('api:create'),
                                kwargs={'pk': 3},
                                format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_tweet(self):
        tweet = Tweet.objects.get()

        response = self.client.get(
            reverse('api:create'),
            kwargs={'pk': tweet.id},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, tweet)

    def test_api_can_update_tweet(self):
        tweet = Tweet.objects.get()
        edit_tweet = {'text': 'It\'s my first tweet!'}

        response = self.client.put(
            reverse('api:details',
                    kwargs={'pk': tweet.id}),
            edit_tweet,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_tweet(self):
        tweet = Tweet.objects.get()

        response = self.client.delete(
            reverse('api:details',
                    kwargs={'pk': tweet.id}),
            format='json',
            follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_comment_tweet(self):
        tweet = Tweet.objects.get()
        print(tweet.id)
        comment_data = {
            'text': 'Allons-y!',
            'parent': tweet.id
        }

        response = self.client.post(
            reverse('api:comment_create'),
            comment_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_comment_a_comment(self):
        self.test_api_can_comment_tweet()

        tweet = Tweet.objects.first()
        comment = tweet.comments.first()

        comment_data = {
            'text': 'Yup!',
            'parent': comment.id
        }

        response = self.client.post(
            reverse('api:comment_create'),
            comment_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
