from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'WXZeQYUF0pMkzCWZvSmLfr6tT'
CONSUMER_SECRET = 'vZcgXztTKwjp24Qg32xNU99QeiMc55IVDKj1zn8eyPCUfMYft4'
OAUTH_TOKEN = '104185612-ObgZvBK6MIGdgigdpdN49VQSyymtTdEsGxuICFvA'
OAUTH_TOKEN_SECRET = 'yWtBbifplYR4wUox9uxBrArWjceYaSS5lFH7iyxF4O4fq'

keyword_list = ['python', 'java', 'c#', 'ruby']  # track list


class MyStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    def on_error(self, status):
        print status
        return True


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)
