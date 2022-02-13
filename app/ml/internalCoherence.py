'''
INTERNAL TOPIC SCORER
FUNC: - User internal topics determined by presence of keyword term
      - PER TWEET = 1 (not multi score within tweet)
      - DENSITY = Multiple tweets per tweet history for user
SEND TO: Final Output

CRUNCH POINTS: 1. Number of keywords - potentially expansive??? 2. Text matching!!!

### VERSION 1: This version inputs only users that have matches with keywords
### VERSION 2: This version will give scores for every keyword for each user
### VERSION 3 (FINAL): Matches score only if alongside organising/campaigning terms
'''

from ml.localityScorer import localUsersDict
from ml.wordNetExpander import keywordsExpanded
from db import db
from models import Tweet, User, KeywordScore, KeywordTweet

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
    - usersDict: {userID: [statusesCount, [tweets]], userID2: [statusesCount, [tweets]]}
    OUTPUT:
    - Topic ranking: per user, per topic
    '''
    users = User.query.all()

    for user in users:
        tweets = Tweet.query.filter(userID=user.id)

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