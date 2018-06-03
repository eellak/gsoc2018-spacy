from gensim.models import FastText
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', 
level=logging.INFO)
sentences = gensim.models.word2vec.LineSentence('dati.txt')
lemma_sentences=[]
with open ('produced_sentences.txt') as fileinst:
	for line in fileinst:
		tmp=line.rstrip()
		lemma_sentences.append(tmp.split(' '))

lemmas_model = FastText(sentences=lemma_sentences, size=100,iter=10,
	window=5,min_count=1, workers=4);
lemmas_model.save('lemmas_model')
