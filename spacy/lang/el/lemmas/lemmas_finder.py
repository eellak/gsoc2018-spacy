import stemmer
import myfuncs
from collections import defaultdict
stemms=defaultdict(list)
input_words=[]
with open("greek_dict.in") as fileinst:
	for line in fileinst:
		input_words.append(myfuncs.strip_accents(line.rstrip()).upper())
for i in input_words:
	stemms[stemmer.stem(i)].append(i)

for key,value in stemms.items():
	print("{} :".format(key),end='')
	for j in value:
		print("{}, ".format(j),end='')
	print()



