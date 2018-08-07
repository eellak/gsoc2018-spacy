# Example: check for urls

import spacy
nlp = spacy.load('el')
text = '''Η ιστοσελίδα για το demo μας είναι: https://nlp.wordames.gr'''
doc = nlp(text)
for token in doc:
    if token.like_url:
        print('Url: {}'.format(token))
