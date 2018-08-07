
import spacy
nlp = spacy.load('el')
doc = nlp("Ο Κώστας αγόρασε πατάτες και τις άφησε πάνω στο ψυγείο.")


for token in doc:
    print('Token:{}, POS tag: {}'.format(token,token.tag_))
