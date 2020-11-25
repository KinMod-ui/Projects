import tweepy
import time

auth = tweepy.OAuthHandler('NfBp2SfzvoSLdG8Mm6IGNiV6g','OvmPebwp4fKMikYXCVkMBH3WDPZsgKFYdtTkWx3UIqUNbTOc8n')

auth.set_access_token('3066578461-GPYXENcnDSY3FzRTh1jKh9VhAoRmAknzjWyc3Sj' , '4aTRcmJu6e9YAVEF7sNtfejCDi6ns3S1bO8jPZ9wxIyF2')

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

