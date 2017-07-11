import tweepy
from tweepy import OAuthHandler
 
consumer_key = '9DG4lRUiCcy0pRtBFc8pQA7Lf'
consumer_secret = 'XGhwdI09tyN6Vvbjqn8sKVyOPIBYJeThqABkI9msc8iRgLJQvc'
access_token = '864738618-MaTgZNHybXaY8DkqKTyaLUlXgRvNkvk5s1Edgmk3'
access_secret = ' 6X5HpAiaO1bifZCEnRDbygLUEj7wSFfB1s2SBywjKXMWM'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)