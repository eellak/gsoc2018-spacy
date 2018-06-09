import spacy
import el_unnamed
import logging
from gensim.corpora import WikiCorpus, MmCorpus
nlp=el_unnamed.load()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
wiki = WikiCorpus("../etc/elwiktionary-latest-pages-articles.xml.bz2",lemmatize=False, dictionary={})
sentences = wiki.get_texts()
counter=0
for sentence in sentences:
	doc=nlp(sentence)
	flag=False
	for i in doc:
		if (i.tag_=='PROPN'):
			flag=True
	if (flag==True):
		counter+=1
		print(sentence)
	if (counter==20000):
		break
