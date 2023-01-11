from matplotlib import pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import pandas as pd
import seaborn as sns

analyzer = SentimentIntensityAnalyzer()

tweet_df = pd.read_csv('csv_data.csv')


#functions that cleans tweets from special characters, links and retweet signs
def cleaner(text):
    text = re.sub("https?://[A-Za-z0-9./]*", "", text)
    text = re.sub("RT @[\w]*:", "", text)
    text = re.sub("(@[A-Za-z0-9_]+)", "", text)
    text = ' '.join(text.split())
    return text


tweet_df['Text'] = tweet_df['Text'].apply(lambda x: cleaner(x))
tweet_df.drop_duplicates(subset=['Text'], keep='first', inplace=True)
tweet_df['Scores'] = tweet_df['Text'].apply(lambda text: analyzer.polarity_scores(text))


def cut(date):
    date = date[:10]
    return date


tweet_df['Date'] = tweet_df['Date'].apply(lambda x: cut(x))

# function that determines sentiment based on compound score
def determine(sentiment):
    if sentiment['compound'] >= 0.05:
        return "Positive"
    elif sentiment['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"


tweet_df['Valence'] = tweet_df['Scores'].apply(lambda x: determine(x))
positive = tweet_df[tweet_df['Valence'] == 'Positive']
negative = tweet_df[tweet_df['Valence'] == 'Negative']
neutral = tweet_df[tweet_df['Valence'] == 'Neutral']
posnumb = len(positive)
negnumb = len(negative)
neutnumb = len(neutral)
total = posnumb + negnumb + neutnumb

print("Information about tweets with keyword posted in the last 7 days")
print("Positive tweets: " + str(posnumb))
print("Negative tweets: " + str(negnumb))
print("Neutral tweets: " + str(neutnumb))

pos_perc = round((posnumb / total) * 100)
neg_perc = round((negnumb / total) * 100)
neut_perc = round((neutnumb / total) * 100)
print("Percentage of positive tweets: " + str(pos_perc) + "%")
print("Percentage of negative tweets: " + str(neg_perc) + "%")
print("Percentage of neutral tweets: " + str(neut_perc) + "%")


sns.countplot(x = 'Valence', data = tweet_df)
plt.title("Total valence of tweets")
plt.show()

sns.countplot(data=tweet_df, x='Date', hue='Valence')
plt.title("Valence of tweets by date")
plt.show()










