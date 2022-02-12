import json
from datetime import datetime

from db import db
from models import User, Tweet

db.create_all()

with open("tweetStructureExample.json", encoding="utf8") as f:
    rawTweet = json.load(f)
    tweet = Tweet(
        id=rawTweet["id"],
        content=rawTweet["content"],
        url=rawTweet["url"],
        date=datetime.fromisoformat(rawTweet["date"]),
        retweetedTweet=True if rawTweet["retweetedTweet"] else False,
        quotedTweet=True if rawTweet["quotedTweet"] else False
    )
    db.session.add(tweet)

    rawUser = rawTweet["user"]
    user = User(
        id=rawUser["id"],
        username=rawUser["username"],
        displayname=rawUser["displayname"],
        location=rawUser["location"],
        rawDescription=rawUser["rawDescription"],
        created=datetime.fromisoformat(rawUser["created"]),
        followersCount=rawUser["followersCount"],
        friendsCount=rawUser["friendsCount"],
        statusesCount=rawUser["statusesCount"],
        profileImageUrl=rawUser["profileImageUrl"],
        profileBannerUrl=rawUser["profileBannerUrl"],
        url=rawUser["url"]
    )
    db.session.add(user)
    db.session.commit()