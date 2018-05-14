with open('adj_norms_3.txt') as fileinst:
	for line in fileinst:
		first_part=line.split(',', 1)[0]
		second_part=line.split('→',1)[1].rstrip().strip()
		if ('νος' in second_part):
			first_part_fixed=first_part.split('ιος')[0]
			second_part_fixed=second_part.split('ος')[0]
			print("{} → {}".format(first_part,second_part))
			print("{} → {}".format(first_part_fixed + 'ια',second_part_fixed+'η'))
			print("{} → {}".format(first_part_fixed + 'ιο',second_part_fixed+'ο'))
		elif ('νός' in second_part):
			first_part_fixed=first_part.split('ιος')[0]
			second_part_fixed=second_part.split('ός')[0]
			print("{} → {}".format(first_part,second_part))
			print("{} → {}".format(first_part_fixed + 'ια',second_part_fixed+'ή'))
			print("{} → {}".format(first_part_fixed + 'ιο',second_part_fixed+'ό'))
		else:
			first_part_fixed=first_part.split('ιος')[0]
			second_part_fixed=second_part.split('ιος')[0]
			print("{} → {}".format(first_part,second_part))
			print("{} → {}".format(first_part_fixed + 'ια',second_part_fixed+'ια'))
			print("{} → {}".format(first_part_fixed + 'ιο',second_part_fixed+'ιο'))
		