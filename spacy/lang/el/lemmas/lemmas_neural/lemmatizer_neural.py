import distance
from gensim.models import FastText
import sys
sys.path.insert(0,"../../");
from lemmatizer import LOOKUP

# Model wiki.el.vec.bin can be downloaded from:
# https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md
model=FastText.load_fasttext_format('wiki.el.bin')


class Relation:
	def __init__(self,dist,text):
		self.distance=dist
		self.word=text


def lemmatizer(word):

	try:
		res=LOOKUP[word]
		return res
	except:
		related_words=model.most_similar(word)
		objects_seq=[]
		for i in related_words:
			dist=distance.levenshtein(word,i)
			objects_seq.append(Relation(dist,i))
		objects_seq.sort(key=lambda x: x.distance)
		for i in objects_seq:
			try:
				res=LOOKUP[i.word]
				return res
			except:
				pass
		return word

def run():
	while(True):
		x=input('Give me word to search lemma\n')
		res=lemmatizer(x)
		print('Lemma: {}'.format(res))

run()




