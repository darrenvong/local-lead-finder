from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
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


class Tweet(Base):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key=True)
    content = Column(String)
    url = Column(String)
    date = Column(DateTime)
    retweetedTweet = Column(Boolean)
    quotedTweet = Column(Boolean)
    # "coordinates": null,
    # "place": null,
    # "hashtags": ["Haringey"]
