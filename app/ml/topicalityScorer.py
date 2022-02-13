'''
INTERNAL TOPIC SCORER
FUNC: - Identifying someone who speaks about topic frequently
'''

from wordNetExpander import keywordsExpanded
from db import db
from models import Tweet, User, KeywordScore, KeywordTweet#, Locality

def commit_keyword_score(keyword, userId, score):
    keyword_score = KeywordScore(userID=userId, keyword=keyword, score=score)
    db.session.add(keyword_score)
    db.session.commit()

def commit_tweet_keyword(keyword, tweetid):
    keyword_tweet = KeywordTweet(keyword=keyword, tweetID=tweetid)
    db.session.add(keyword_tweet)
    db.session.commit()

def topicScore(keywordsExpanded):
    '''
    INPUT: 
    - Keywords with WordNet expanded terms - keywordsExpanded
    - Filtered local users & their tweets
    OUTPUT:
    - Score indicating how much a user discusses topic
    '''
    users = User.query.all()
    #users = Locality.query.filter_by(locality='y')

    for user in users:
        tweets = Tweet.query.filter_by(userID=user.id)

        ### This section is for searching for all keyword
        for key in keywordsExpanded.keys():
            keywordScore = 0
            for tweet in tweets:
                tweet.lower()
                for val in key:
                    val.lower()
                    if val in tweet.content:
                        keywordScore += 1
                        commit_tweet_keyword(key, tweet)
            commit_keyword_score(key, user, keywordScore)