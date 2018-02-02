# Code that generates sentiment analysis on artists of various genres 


import sys
reload(sys)
sys.setdefaultencoding('utf8')

import tweepy
import twitter
from twitter import *
from textblob import TextBlob




# Consumer keys and access tokens, used for OAuth

consumer_key = 'V05ugHAiPq4GSHLoR1gxo8mch'
consumer_secret = 'SyU5J8gmWRnypSz6bNCRlxrkGx5qhjKl9FHdBPTa31fewNZBmD'


access_token = '838092579568828417-7VAJWiVhFw3RPDUrZPhTQAfI8J2YGdd'
access_token_secret = '8GZy8qA6z21u968EW9YVnI8g8MYxMt0lVTm99V5lAxVLH'



# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)


#sentiment analysis + printing the results using the tweepy search api
public_tweets1 = api.search('Green Day')

for tweet in public_tweets1:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 


public_tweets2 = api.search('Kanye West')

for tweet in public_tweets2:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 



public_tweets3 = api.search('Coldplay')

for tweet in public_tweets3:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 



public_tweets4 = api.search('Bruno Mars')

for tweet in public_tweets4:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 

public_tweets5 = api.search('Kendrick Lamar')

for tweet in public_tweets5:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 




public_tweets6 = api.search('Rihanna')

for tweet in public_tweets6:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 


#Filter out tweet results that are irrelevant to the actual artist "Future"
   #ex:  *filter out tweets such as : I'm so excited about my future!
public_tweets7 = api.search('Future')

for tweet in public_tweets7:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 




public_tweets8 = api.search('Taylor Swift')

for tweet in public_tweets8:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 




public_tweets9 = api.search('Luke Bryan')

for tweet in public_tweets9:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 



public_tweets10 = api.search('Justin Bieber')

for tweet in public_tweets10:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment) 








