#!/usr/bin/env python
import sys
import os
sys.path.append('lib/tweepy')

from lib.tweepy import tweepy
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://dev.twitter.com and create an app. 
# The consumer key and secret will be generated for you after
consumer_key = 'T6nfdEvNMdcJaNM49B5bQ'
consumer_secret = 'VyE4C9RKNtTqOPYaFhUSGRFS7q1S8fZy5FxWovH6AU'

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=''
access_token_secret=''

class StdOutListener(StreamListener):
	""" A listener handles tweets are the received from the stream. 
	This is a basic listener that just prints received tweets to stdout.

	"""
	def on_data(self, data):
		play = os.popen("madplay twitter.mp3")
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = Stream(auth, l)	
	stream.filter(follow=[210885928])
