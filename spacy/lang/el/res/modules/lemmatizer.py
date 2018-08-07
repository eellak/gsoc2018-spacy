# Example: lemmatizer example

import spacy
nlp = spacy.load('el')
text = '''Τα σύμβολα του αγώνα.'''
doc = nlp(text)
for token in doc:
    print("Original token: {} , Lemma: {}".format(token,token.lemma_))
