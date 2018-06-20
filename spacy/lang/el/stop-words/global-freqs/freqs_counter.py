import re
import operator
from collections import defaultdict
import unicodedata
import sys
sys.path.insert(0,"../etc");
import myfuncs
import logging
from gensim.corpora import WikiCorpus, MmCorpus

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

wiki = WikiCorpus("../res/elwiki-latest-pages-articles.xml.bz2",lemmatize=False, dictionary={})


word_times=defaultdict(int) # number of times each word occurs
word_documents=defaultdict(int) # number of documents in each a word occurs
sentences = list(wiki.get_texts())
for sentence in sentences:
	unique_words=set([])
	for word in sentence:
		word_times[word]+=1
		unique_words.add(word)
	for i in unique_words:
		word_documents[i]+=1


# sorted based on their frequencies
sorted_words_list=sorted(word_times.items(),key=operator.itemgetter(1),reverse=True)
for i in sorted_words_list:
	curr_key=i[0]
	if (len(curr_key)>1):
		print("{} {} \'{}\'".format(word_times[curr_key],word_documents[curr_key],myfuncs.get_accent(curr_key)))

