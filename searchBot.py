import tweepy                                                           #import tweepy library
import time

#security details below
CONSUMER_KEY = ''
CONSUMER_SECRET=''
ACCESS_KEY=''
ACCESS_SECRET=''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)            #authentication on twitter happens here.

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True )                        #create an API object from API class


         #trying the @ for userID in a tweet and testing if it works'  
tweetNumber = 500000

tweets = tweepy.Cursor(api.search, q= ('#microbit OR #micropython OR @MSMAKECODE')).items(tweetNumber)

def searchBot():



    for tweet in tweets:
        try:
            tweet.retweet()     #retweet
            tweet.favorite()    #like the tweet
            print(tweet.id,'retweet done')

            time.sleep(120)
        except tweepy.TweepError as e:
            print(tweet.id)
            print(e.reason)

            time.sleep(60)
        except StopIteration:
            break
searchBot()

