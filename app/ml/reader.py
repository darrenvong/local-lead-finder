'''
LOCALITY TERMS
FUNC: Read our textfiles with locality terms
INPUT: .txt files
OUTPUT: localityTerms as list

SENT TO: LocalityScorer
'''

with open("streets.txt", "r") as f:
    text = f.read()

localityTerms = text.split("\n")

## https://geographic.org/streetview/uk/Haringey_London_Boro/index.html

print(localityTerms)