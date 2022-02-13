from sqlalchemy import BigInteger, Column, Integer, String, DateTime, Boolean, ForeignKey

from db import db


class User(db.Model):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)
    username = Column(String)
    displayname = Column(String)
    location = Column(String)
    rawDescription = Column(String)
    created = Column(DateTime)
    followersCount = Column(Integer)
    friendsCount = Column(Integer)
    statusesCount = Column(Integer)
    profileImageUrl = Column(String)
    profileBannerUrl = Column(String)
    url = Column(String)


class Tweet(db.Model):
    __tablename__ = 'tweet'

    id = Column(BigInteger, primary_key=True)
    userID = Column(BigInteger, ForeignKey('user.id'), nullable=False)
    content = Column(String)
    url = Column(String)
    date = Column(DateTime)
    retweetedTweet = Column(Boolean)
    quotedTweet = Column(Boolean)
    # "coordinates": null,
    # "place": null,
    # "hashtags": ["Haringey"]
