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
    def get_user(cls, current_id):
        return db.session.query(User).filter(User.id == current_id)


class Tweet(db.Model):
    __tablename__ = 'tweet'

    id = Column(BigInteger, primary_key=True)
    content = Column(String)
    url = Column(String)
    date = Column(DateTime)
    retweetedTweet = Column(Boolean)
    quotedTweet = Column(Boolean)
    # "coordinates": null,
    # "place": null,
    # "hashtags": ["Haringey"]
