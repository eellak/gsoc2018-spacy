import sys
sys.path.insert(0,"../")
import stemmer
from random import shuffle
import random
sys.path.insert(0,"../../etc");
import myfuncs
from collections import defaultdict
stemms=defaultdict(list)
# input_words: list with all the words in the "stemmer version"
input_words=[]
lemmas=defaultdict(lambda:'null')
matched=defaultdict(list)
# recover: dictionary with keys the "stemmer versioned" words and values their
# original value.
recover=defaultdict(lambda:'null') 
with open("../../etc/greek_dict.in") as fileinst:
	for line in fileinst:
		tmp=myfuncs.strip_accents(line.rstrip()).upper()
		recover[tmp]=line.rstrip()
		input_words.append(tmp)

with open("../merged.out") as fileinst:
	for line in fileinst:
		tmp=myfuncs.strip_accents(line.rstrip()).upper()
		lemmas[tmp]="not null"
		recover[tmp]=line.rstrip()


for i in input_words:
	stemms[stemmer.stem(i)].append(i)

for key,value in stemms.items():
	found=0
	for j in value:
		if (lemmas[j]!="null"):
			found=j
			break
	if (found!=0):
		for j in value:
			matched[recover[found]].append(recover[j])

with open('produced_sentences.txt','a') as fileinst:
	for key,values in matched.items():
		times=random.randint(10,16)
		currLength=len(values)
		for x in range(times):
			end=random.randint(0,currLength)
			shuffle(values)
			if (end!=0):
				fileinst.write(' '.join(values[0:end]))
				fileinst.write("\n")


