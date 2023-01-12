## Description
The program scrapes most recent tweets (posted in the last 7 days) that include a specific keyword .
Tweets are then cleaned from links and special characters and duplicates are removed.
Afterwards, sentiment analysis is performed using VADER-software.

## Usage

```
pip install -r requirements.txt
export TWITTER_BEARER_TOKEN=<insert your bearer token>
# to download tweets posted in last 7 days with specified keyword:
./scrape.py
# to perform sentiment analysis:
./analysis.py

```
## Example (Keyword: "Munich")
The following results are produced:

<img src="https://github.com/yomostova/TwitterKeyword-VADER-analysis/blob/master/Screenshot%202023-01-12%20at%2000.10.16.png" width="500" height="150">


<img src="https://github.com/yomostova/TwitterKeyword-VADER-analysis/blob/06281f41ac2c88ae0347d437cfabdb1520403907/Screenshot%202023-01-12%20at%2000.09.12.png" width="500" height="400">

<img src="https://github.com/yomostova/TwitterKeyword-VADER-analysis/blob/06281f41ac2c88ae0347d437cfabdb1520403907/Screenshot%202023-01-12%20at%2000.09.51.png" width="500" height="400">



### Citations

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
