# ents example


import spacy
nlp  = spacy.load('el')
text = '''Η εταιρεία Google έχει τα γραφεία της στην Καλιφόρνια.'''
doc = nlp(text)
for ent in doc.ents:
  print("Entity:{}, Label:{}".format(ent.text, ent.label_))
