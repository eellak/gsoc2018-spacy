import distance
import time
from gensim.models import KeyedVectors   
from collections import defaultdict
import unicodedata


input_words=[]
start_time=time.time()
fmodel = KeyedVectors.load_word2vec_format('cc.el.300.vec',limit=100000)


with open("greek_dict.in") as fileinst:
	for line in fileinst:
		input_words.append(line.rstrip())
j=0
for i in input_words:
	try:
		most_similar=unicodedata.normalize('NFD',(fmodel.most_similar(i)[0][0]).lower())
		if (distance.levenshtein(unicodedata.normalize('NFD',i.lower()),most_similar)<=1):
			print("{} : {}".format(i,most_similar),flush=True)
	except:
		j+=1


end_time=time.time()
print('{} words not found'.format(j),flush=True)
print(end_time-start_time,flush=True)