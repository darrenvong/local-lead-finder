'''
LOCALITY SPECIFIER
FUNC: Confirmation of probable locality
SEND TO: 
- Internal Coherence
'''
from ml.reader import localityTerms

def localityScore(usersDict, localityTerms):

    '''
    INPUT: 
    - usersDict: {userID: [statusesCount, [tweets]], userID2: [statusesCount, [tweets]]}
    - localityTerms = [terms]

    OUTPUT:
    - localUsersDict
    '''

    localUsersDict = {}
    localUsersDict[userID] = []

    for user in usersDict.keys():
        localityScore = 0
        for l in localityTerms:
            for tweet in user[1]:
                if l in tweet:
                    localityScore += 1
                    continue

        if localityScore > 5:
            local = Y
            def commit_local_user(userID, local):
            pass

    return localUsersDict



