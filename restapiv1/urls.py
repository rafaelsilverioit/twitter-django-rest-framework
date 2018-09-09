from django.urls import path
from .views import ListTweetView, ListCreateTweetView, ListUpdateDeleteTweetView


app_name = 'api'
urlpatterns = [
    path('api/v1/tweet/', ListCreateTweetView.as_view(), name='create'),
    path('api/v1/tweet/public', ListTweetView.as_view(), name='public'),
    path('api/v1/tweet/<int:pk>/', ListUpdateDeleteTweetView.as_view(), name='details'),
]
