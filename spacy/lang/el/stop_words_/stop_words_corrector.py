from collections import defaultdict
import sys
sys.path.insert(0,"../etc/");
import myfuncs

all_words=defaultdict(lambda: '')
with open("../etc/greek_dict.in") as fileinst:
	for line in fileinst:
		all_words[myfuncs.strip_accents(line.rstrip())]=line.rstrip()
out=defaultdict(lambda:'')
with open("stop_words_without_accents.out") as fileinst:
	for line in fileinst:
		for x in line.rstrip().split():
			if (all_words[x]!=''):
				out[x]=all_words[x]

previous='α'
# sorts strings after removing accents
for i in sorted(out.keys()):
	# new line when letter changes
	if (out[i][0]!=previous):
		previous=out[i][0]
		print()
	print("{} ".format(out[i]),end='') 
