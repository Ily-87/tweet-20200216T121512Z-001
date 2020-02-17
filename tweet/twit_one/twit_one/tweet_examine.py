import json
import re
import pandas
import matplotlib.pyplot as plt

tweets_data_path = "tweet_mining.json"

def read_json(file_path):
    results = []
    tweets_file = open(tweets_data_path, "r")
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue
    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

results = read_json(tweets_data_path)

statuses = pandas.DataFrame()

statuses['text'] = map(lambda status: status['text'], results)
statuses['lang'] = map(lambda status: status['lang'], results)
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python',status))
statuses['java'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('java', status))
statuses['c#'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#',status))
statuses['ruby'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('ruby', status))

# output the number of tweets where it is True that they contain our keywords

slices =[]
slices.append(statuses['python'].value_counts()[True])
slices.append(statuses['java'].value_counts()[True])
slices.append(statuses['c#'].value_counts()[True])
slices.append(statuses['ruby'].value_counts()[True])


keywords = ['python', 'java', 'c#', 'ruby']
cols = ['c','m','r','b']
plt.pie(slices, labels=keywords, colors=cols, startangle=90, shadow=True, explode=(0,0,0,0), autopct='%1.1f%%')
plt.show()
