'''
WORDNET KEYWORD EXPANDER
FUNC: Expands a series of keywords into broader synonym terms
'''

from nltk.corpus import wordnet as wn
from itertools import chain

keywords = ['tree', 'climate', 'rubbish', 'Haringey']

def keywordExpansion(keywords):

    '''
    INPUT: Keywords as list
    OUTPUT: Expand dict with lists {keyword1: [expanded_list], keyword2: [expanded_list2]}
    '''
    keywordsExpanded = {}

    for keyword in keywords:

        synonyms = wn.synsets(keyword, pos=wn.NOUN, lang='eng')
        lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
        lemmas.add(keyword)
        keywordsExpanded[keyword] = lemmas

    return keywordsExpanded