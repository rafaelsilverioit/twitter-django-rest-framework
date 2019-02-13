[![Build Status](https://semaphoreci.com/api/v1/rafaelsilverioit/twitter-django-rest-framework/branches/master/badge.svg)](https://semaphoreci.com/rafaelsilverioit/twitter-django-rest-framework)

# twitter-django-rest-framework

Building a simple Twitter like app with Django Rest Framework for the backend and hopefully (haven't decided yet) React with Materialize for the frontend.

Done:

* Rest API with all tweet handling endpoints, business logic, authentication and authorization.
  * Tweet management: Users can read any public available tweet and create, update and delete their own tweets only;
  * Privacy settings (public or private): Users can set only their tweets to public or private;
  * Comments and nested comments: Users can comment in any public available comment and reply to other comments. Users can create, update and delete their own comments only;
  * Likes: Users can like and dislike any public available tweet;
  * Authentication and authorization for the API: Whenever a new user is created, an authentication token is also created for that user. As mentioned above, all user authorization measures needed so far were implemented.

Todo:

* Retweets;
* Search engine (for tweets, trend topics and users);
* User account management;
* User friendship (follow and unfollow);
* Trend topics;
* Accept images (jpg, png and gif);
* Detect links and show a preview;
* Embed Youtube videos.
* A cool web interface for the API. Thinking about React with Materialize;
* MORE TESTS.
