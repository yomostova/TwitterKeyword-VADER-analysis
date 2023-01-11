import tweepy
from dotenv import load_dotenv
import os
import pandas as pd
import datetime

load_dotenv()
token = os.environ.get("TWITTER_BEARER_TOKEN")
client = tweepy.Client(token)
keyword = input("Hello! Which topic do you want to analyze? Please give one keyword: ")


def search(keyword, endtime: datetime.datetime):
    tweets = []
    endtime.isoformat()
    r = client.search_recent_tweets(keyword + " - is:retweet", end_time=endtime.isoformat(), max_results=100,
                                         tweet_fields=['author_id', 'created_at', 'text', 'public_metrics'])
    tweets.extend(r.data)
    tweet_details = []
    for tweet in tweets:
        tweet_details.append({"Text": tweet.text,
                              "User": tweet.author_id,
                              "Date": tweet.created_at,
                              "Likes": tweet.public_metrics.get("like_count")
                              })
    return tweet_details


dates = []

now = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=10)
dates.append(now)
for day in range(1, 7):
    x = (now - datetime.timedelta(days=day))
    dates.append(x)

all_tweets = []
for date in dates:
    all_tweets.extend(search(keyword, date))

tweet_df = pd.DataFrame(data=all_tweets, columns=["Text", "User", "Date", "Likes"])

# save scraped data into csv
with open('csv_data.csv', 'w') as csv_file:
    tweet_df.to_csv(path_or_buf=csv_file)