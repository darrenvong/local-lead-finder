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

    @classmethod
    def is_user_exists(cls, current_id):
        return db.session.query(User).filter(User.id == current_id).count()


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

class KeywordScore(db.model):
    __tablename__ = 'keywordScore'

    id = Column(BigInteger, primary_key=True)
    userID = Column(BigInteger, ForeignKey('user.id'), nullable=False)
    keyword = Column(String)
    score = Column(Integer)

class KeywordTweet(db.model):
    __tablename__ = 'keywordTweet'

    id = Column(BigInteger, primary_key=True)
    keyword = Column(String)
    tweetID = Column(BigInteger, ForeignKey('tweet.id'), nullable=False)