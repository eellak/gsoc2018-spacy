with open('norms_from_dict.txt') as fileinst:
	for line in fileinst:
		if (not 'ιιι' in line):
			print(line.rstrip())