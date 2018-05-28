import stemmer
import sys
sys.path.insert(0,"../etc");
import myfuncs
from collections import defaultdict
stemms=defaultdict(list)
input_words=[]
lemmas=defaultdict(lambda:'null')
not_matched=[]
matched=[]
recover=defaultdict(lambda:'null')
with open("../etc/greek_dict.in") as fileinst:
	for line in fileinst:
		tmp=myfuncs.strip_accents(line.rstrip()).upper()
		recover[tmp]=line.rstrip()
		input_words.append(tmp)

with open("merged.out") as fileinst:
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
	if (found==0):
		not_matched.append(key)
	else:
		for j in value:
			if (j!=found):
				matched.append([recover[j],recover[found]])

with open('matched.txt','a') as fileinst:
	for x in matched:
		fileinst.write("\"{}\":\"{}\"".format(x[0],x[1]))
		fileinst.write("\n")

with open('not_matched.txt','a') as fileinst:
	for x in not_matched:
		fileinst.write(x)
		fileinst.write('\n')

