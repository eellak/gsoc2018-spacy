# this file merges lemmas from different sources

out=[]
with open('elwords_from_wiktionary.txt') as fileinst:
	for line in fileinst:
		check=line.split(' ')
		if (len(check)==1):
			out.append(line.rsplit()[0])

with open('lemmas_out_of_wiktionary/lemmas.out') as fileinst:
	for line in fileinst:
		check=line.split(' ')
		if (len(check)==1):
			out.append(line.rsplit()[0])

# remove duplicates
out=set(out)
for i in out:
	print(i)