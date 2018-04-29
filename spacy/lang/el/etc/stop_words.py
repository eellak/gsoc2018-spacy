import re
import operator
from collections import defaultdict
import unicodedata

# english language about 300 stop-words.
num_of_words=300
my_dict=defaultdict(int)
with open("text.in") as fileinst:
	for line in fileinst:
		# keep only alphanumeric characters
		processed_line=list(re.sub(r'[^\w]',' ',line).lower().split())
		for k in processed_line:
			my_dict[k]+=1
# sorted based on their frequencies
sorted_tuple=sorted(my_dict.items(),key=operator.itemgetter(1),reverse=True)
count=0
my_list=[]
for i in sorted_tuple:
	if (count>num_of_words):
		break
	count+=1
	if (len(i[0])>1):
		my_list.append(i[0])
previous='α'
# sorts strings after removing accents
for i in sorted(my_list,key=lambda x: unicodedata.normalize('NFD',x)):
	# new line when letter changes
	if (i[0]!=previous):
		previous=i[0]
		print()
	print("{} ".format(i),end='') 