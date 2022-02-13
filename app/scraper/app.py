import snscrape.modules.twitter as sntwitter
from pprint import pprint as pp

from models import *

def scrape_tweets(query, max_tries):
    tweets = []

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i>max_tries:
            break
        tweets.append(tweet)

    return tweets


if __name__ == "__main__":   
    tweets = scrape_tweets("COVID :2022-02-10 until:2022-02-11", 10)

    for t in tweets:
        print(t.content)

# 'url', 'date', 'content', 'renderedContent', 'id', 'user', 'replyCount', 'retweetCount',
#  'likeCount', 'quoteCount', 'conversationId', 'lang', 'source', 'sourceUrl', 'sourceLabel',
#  'outlinks', 'tcooutlinks', 'media', 'retweetedTweet', 'quotedTweet', 'inReplyToTweetId',
#  'inReplyToUser', 'mentionedUsers', 'coordinates', 'place', 'hashtags', 'cashtags']