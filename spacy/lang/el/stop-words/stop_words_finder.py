import re
import operator
import unicodedata
import sys

# keep about 350 words
words=[]
num_of_words = 350
count=1
with open('global-freqs/out.txt') as fileinst:
    for line in fileinst:
        tmp_line=line.rsplit()
        count+=1
        words.append(tmp_line[2].replace('\'',''))
        if (count==350):
            break
    

words=sorted(words)
previous='α'
with open('stop_words.out','w') as fileinst:
    for i in sorted(words):
        # new line when letter changes
        if (i[0]!=previous):
            previous=i[0]
            fileinst.write('\n')
        fileinst.write("{} ".format(i)) 
