import spacy
import re
nlp = spacy.load('el')
text = '''Η όμορφη ιδέα του άλλαξε την μίζερη ζωή.'''
# remove punct
chunks = [re.sub(r'[^\w\s]', '', x.text) for x in nlp(text).noun_chunks]
for chunk in chunks:
    print(chunk)
