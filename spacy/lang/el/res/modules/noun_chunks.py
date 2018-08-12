import spacy
import re
nlp = spacy.load('el')
text = '''Η μικρή σιγή. Την ένιωσα δίπλα μου την απόλυτη σιωπή. Αυτή που
σκεπάζει το άπειρο.'''

chunks = [re.sub(r'[^\w\s]', '', x.text) for x in nlp(text).noun_chunks]
for chunk in chunks:
    print(chunk)
