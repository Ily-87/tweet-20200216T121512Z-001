import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'WXZeQYUF0pMkzCWZvSmLfr6tT'
CONSUMER_SECRET = 'vZcgXztTKwjp24Qg32xNU99QeiMc55IVDKj1zn8eyPCUfMYft4'
OAUTH_TOKEN = '104185612-ObgZvBK6MIGdgigdpdN49VQSyymtTdEsGxuICFvA'
OAUTH_TOKEN_SECRET = 'yWtBbifplYR4wUox9uxBrArWjceYaSS5lFH7iyxF4O4fq'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print (common_trends)
