# sentence splitting example

import spacy
nlp = spacy.load('el')
text = ''' Αυτή είναι μια πρόταση. Αυτή είναι μια δεύτερη πρόταση. Και αυτή μια τρίτη πρόταση.'''
doc = nlp(text)
sentences = list(doc.sents)
print(sentences)
