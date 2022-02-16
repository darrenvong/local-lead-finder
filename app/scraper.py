import json
from pprint import pprint as pp

import snscrape.modules.twitter as sntwitter

from app import db
from models import Tweet, User


def map_tweet_to_db(raw_tweet):
    raw_user = raw_tweet.user
    if not User.is_exists(raw_user.id):
        user = User(
            id=raw_user.id,
            username=raw_user.username,
            displayname=raw_user.displayname,
            location=raw_user.location,
            rawDescription=raw_user.rawDescription,
            created=raw_user.created,
            followersCount=raw_user.followersCount,
            friendsCount=raw_user.friendsCount,
            statusesCount=raw_user.statusesCount,
            profileImageUrl=raw_user.profileImageUrl,
            profileBannerUrl=raw_user.profileBannerUrl,
            url=raw_user.url
        )
        db.session.add(user)
        db.session.commit()

    if not Tweet.is_exists(raw_tweet.id):
        tweet = Tweet(
            id=raw_tweet.id,
            content=raw_tweet.content,
            url=raw_tweet.url,
            date=raw_tweet.date,
            retweetedTweet=True if raw_tweet.retweetedTweet else False,
            userID=raw_tweet.user.id,
            quotedTweet=True if raw_tweet.quotedTweet else False
        )
        db.session.add(tweet)
        db.session.commit()


def scrape_tweets(query, max_tries):
    tweets = []

    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i>max_tries:
            break
        tweets.append(tweet)

    return tweets


if __name__ == "__main__":
    db.create_all()
    print("scraping Tweets")
    tweets = scrape_tweets("london :2022-02-1 until:2022-02-13", 1000)

    for t in tweets:
        print(t.content)
        map_tweet_to_db(t)