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

def commit_keyword_score(keyword, userId, score):
    pass

def commit_tweet_keyword(keyword, tweetid):
    pass

def topicScore(localUsersDict, keywordsExpanded, currentKeyword = 0): #, leaderTerms = 0):
    '''
    INPUT: 
    - Keywords with WordNet expanded terms - keywordsExpanded
    - usersDict: {userID: [statusesCount, [tweets]], userID2: [statusesCount, [tweets]]}
    OUTPUT:
    - Topic ranking: per user, per topic
    '''
    for userID, tweets in localUsersDict.items(): 

        ### This section is for searching for all keywords
        elif currentKeyword == 0:
            for key in keywordsExpanded.keys():
                keywordScore = 0
                for tweet in tweets:
                    for val in key:
                        if val in tweet.lower():
                            keywordScore += 1
                            commit_tweet_keyword(key, tweet)
                commit_keyword_score(key, userID, keywordScore)
                




    

