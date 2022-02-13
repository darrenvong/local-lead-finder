import json
from datetime import datetime

import snscrape.modules.twitter as sntwitter

from db import db
from pprint import pprint as pp
from models import Tweet, User


db.create_all()

def map_tweet_to_db(raw_tweet):
    tweet = Tweet(
        id=raw_tweet["id"],
        content=raw_tweet["content"],
        url=raw_tweet["url"],
        date=datetime.fromisoformat(raw_tweet["date"]),
        retweetedTweet=True if raw_tweet["retweetedTweet"] else False,
        quotedTweet=True if raw_tweet["quotedTweet"] else False
    )
    db.session.add(tweet)

    raw_user = raw_tweet["user"]
    user = User(
        id=raw_user["id"],
        username=raw_user["username"],
        displayname=raw_user["displayname"],
        location=raw_user["location"],
        rawDescription=raw_user["rawDescription"],
        created=datetime.fromisoformat(raw_user["created"]),
        followersCount=raw_user["followersCount"],
        friendsCount=raw_user["friendsCount"],
        statusesCount=raw_user["statusesCount"],
        profileImageUrl=raw_user["profileImageUrl"],
        profileBannerUrl=raw_user["profileBannerUrl"],
        url=raw_user["url"]
    )
    db.session.add(user)
    db.session.commit()


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
        # map_tweet_to_db(t)
        #u = sntwitter.TwitterProfileScraper(t.user).get_items()
        # import pdb;pdb.set_trace()
        # tweet_user = User(

        # )
        # tweet_model = Tweet(
        #     id=t.id,
        #     content=t.content,
        #     url=t.url,
        #     date=t.date,
        #     retweetedTweet=t.retweetedTweet,
        #     quotedTweet=t.quotedTweet
        # )


        # print(tweet_model)

# 'url', 'date', 'content', 'renderedContent', 'id', 'user', 'replyCount', 'retweetCount',
#  'likeCount', 'quoteCount', 'conversationId', 'lang', 'source', 'sourceUrl', 'sourceLabel',
#  'outlinks', 'tcooutlinks', 'media', 'retweetedTweet', 'quotedTweet', 'inReplyToTweetId',
#  'inReplyToUser', 'mentionedUsers', 'coordinates', 'place', 'hashtags', 'cashtags']
