with open('adj_norms_1.txt') as fileinst:
	for line in fileinst:
		first_part=line.split(',', 1)[0]
		second_part=line.split('→',1)[1].rstrip().strip()
		if ('ός' in first_part and 'ός' in second_part):
			first_part_fixed=first_part.split('ός')[0]
			second_part_fixed=second_part.split('ός')[0]
			print("{} → {}".format(first_part,second_part))
			print("{} → {}".format(first_part_fixed + 'ή',second_part_fixed+'ή'))
			print("{} → {}".format(first_part_fixed + 'ό',second_part_fixed+'ό'))
		elif('ος' in first_part and 'ος' in second_part):
			first_part_fixed=first_part.split('ος')[0]
			second_part_fixed=second_part.split('ος')[0]
			print("{} → {}".format(first_part,second_part))
			print("{} → {}".format(first_part_fixed + 'η',second_part_fixed+'η'))
			print("{} → {}".format(first_part_fixed + 'ο',second_part_fixed+'ο'))
		elif ('ος' in first_part and 'ός' in second_part):
			first_part_fixed=first_part.split('ος')[0]
			second_part_fixed=second_part.split('ός')[0]
			print("{} → {}".format(first_part,second_part))
			print("{} → {}".format(first_part_fixed + 'η',second_part_fixed+'ή'))
			print("{} → {}".format(first_part_fixed + 'ο',second_part_fixed+'ό'))
		else:
			first_part_fixed=first_part.split('ός')[0]
			second_part_fixed=second_part.split('ος')[0]
			print("{} → {}".format(first_part,second_part))
			print("{} → {}".format(first_part_fixed + 'ή',second_part_fixed+'η'))
			print("{} → {}".format(first_part_fixed + 'ό',second_part_fixed+'ο'))
