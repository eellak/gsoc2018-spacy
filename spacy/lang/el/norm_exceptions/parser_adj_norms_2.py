with open('adj_norms_2.txt') as fileinst:
	for line in fileinst:
		first_part=line.split(',', 1)[0]
		second_part=line.split('→',1)[1].rstrip().strip()
		first_part_fixed=first_part.split('ος')[0]
		second_part_fixed=second_part.split('ος')[0]
		print("{} → {}".format(first_part,second_part))
		print("{} → {}".format(first_part_fixed + 'α',second_part_fixed+'α'))
		print("{} → {}".format(first_part_fixed + 'ο',second_part_fixed+'ο'))
		