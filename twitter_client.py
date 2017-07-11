# Chap02-03/twitter_client.py
import os
import sys
from tweepy import API
from tweepy import OAuthHandler
consumer_key = '9DG4lRUiCcy0pRtBFc8pQA7Lf'
consumer_secret = 'XGhwdI09tyN6Vvbjqn8sKVyOPIBYJeThqABkI9msc8iRgLJQvc'
access_token = '864738618-MaTgZNHybXaY8DkqKTyaLUlXgRvNkvk5s1Edgmk3'
access_secret = '6X5HpAiaO1bifZCEnRDbygLUEj7wSFfB1s2SBywjKXMWM'
def get_twitter_auth():
    """Setup Twitter authentication.
    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key = ['9DG4lRUiCcy0pRtBFc8pQA7Lf']
        consumer_secret = ['XGhwdI09tyN6Vvbjqn8sKVyOPIBYJeThqABkI9msc8iRgLJQvc']
        access_token = ['864738618-MaTgZNHybXaY8DkqKTyaLUlXgRvNkvk5s1Edgmk3']
        access_secret = ['6X5HpAiaO1bifZCEnRDbygLUEj7wSFfB1s2SBywjKXMWM']
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.
    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client