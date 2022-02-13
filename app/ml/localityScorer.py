'''
LOCALITY SPECIFIER
FUNC: Confirmation of probable locality
'''
from reader import localityTerms
from db import db
from models import Tweet, User, Locality

def commit_local_user(userID, locality):
    local_user = Locality(userID=userID, local=locality)
    db.session.add(local_user)
    db.session.commit()

def localityScore(localityTerms):
    '''
    INPUT: 
    - Users, Tweets
    OUTPUT:
    - Local users
    '''

    users = User.query.all()

    for user in users:
        tweets = Tweet.query.filter(userID=user.id)
        localityScore = 0
        for l in localityTerms:
            for tweet in tweets:
                if l in tweet.content:
                    localityScore += 1
                    break

        if localityScore > 0:
            local = 'y'
            commit_local_user(user, local)



