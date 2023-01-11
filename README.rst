The program scrapes most recent tweets that include a specific keyword posted in the last 7 days.
Tweets are then cleaned from links and special characters and duplicates are removed.
Afterwards, sentiment analysis is performed using VADER-software.

### Usage

```

export TWITTER_BEARER_TOKEN=<insert your bearer token>

# to download tweets posted in last 7 days with specified keyword

./scrape.py

# to perform sentiment analysis

./analysis.py

```

### Citations

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.