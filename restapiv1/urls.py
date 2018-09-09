from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *


app_name = 'api'
urlpatterns = [
    path('api/v1/tweet/', ListCreateTweetView.as_view(), name='create'),
    path('api/v1/tweet/likes/', CreateDeleteLikeView.as_view(), name='like'),
    path('api/v1/tweet/comments/', CreateCommentView.as_view(), name='comment_create'),
    path('api/v1/tweet/comments/<int:pk>/', ListUpdateDeleteCommentView.as_view(), name='comment_details'),
    path('api/v1/tweet/public/', ListPublicTweetsView.as_view(), name='public_tweets'),
    path('api/v1/tweet/<int:pk>/', ListUpdateDeleteTweetView.as_view(), name='details'),
    path('api/v1/get-token/', obtain_auth_token),
]
