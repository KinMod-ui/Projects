import tweepy
import time

removed auth lines >.<

api = tweepy.API(auth , wait_on_rate_limit=True , wait_on_rate_limit_notify=True)

user = api.me()

# print(user.screen_name)

# for follower in tweepy.Cursor(api.followers).items():
#   follower.follow()

search = 'Casey Neistat'

nrTweets = 500

for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
  try:
    print("tweet Liked")
    tweet.retweet()
    time.sleep(10)
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break

