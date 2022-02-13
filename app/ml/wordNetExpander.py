'''
WORDNET KEYWORD EXPANDER
FUNC: Expands a series of keywords into broader synonym terms
SEND TO: Internal Coherence (for scoring users by number of mentions)
'''

from nltk.corpus import wordnet as wn
from itertools import chain

keywords = ['tree', 'climate change', 'rubbish', 'football', 'tennis']

def keywordExpansion(keywords):

    '''
    INPUT: Keywords as list
    OUTPUT: Expand dict with lists {keyword1: [expanded_list], keyword2: [expanded_list2]}
    '''
    keywordsExpanded = {}

    for keyword in keywords:

        synonyms = wn.synsets(keyword, pos=wn.NOUN, lang='eng')
        hyponyms = synonyms[0].hyponyms()
        lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
        #ADD ACTUAL KEYWORD AS WELL AS LEMMAS
        keywordsExpanded[keyword] = lemmas

    return keywordsExpanded

print(keywordExpansion(keywords))