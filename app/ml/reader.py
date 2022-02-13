'''
LOCALITY TERMS
FUNC: Read in locality terms
'''

## https://geographic.org/streetview/uk/Haringey_London_Boro/index.html

with open("streets.txt", "r") as f:
    text = f.read()

localityTerms = text.split("\n")