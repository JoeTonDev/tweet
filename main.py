import schedule
import time
import tweepy

def post_to_twitter(message):
  # Authenticate to Twitter API
  auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
  auth.set_access_token("access_token", "access_token_secret")
  
  #Create API object
  api = tweepy.API(auth)
  
  #Post message to Twitter
  api.update_status(message)
  
# Schedule a tweet to be posted everyday at 9am
schedule.every().day.at("9:00").do(post_to_twitter, message="Good morning! Time to start the day!")

# Start scheduling
while True:
  schedule.run_pending()
  time.sleep(1)