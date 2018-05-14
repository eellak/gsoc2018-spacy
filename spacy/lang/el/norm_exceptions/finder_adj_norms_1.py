with open("norms_from_dict.out") as fileinst:
	for line in fileinst:
		if ("-η, -ο" in line or ('-ή, -ό') in line or ('-ή, -ο') in line or ('-η, -ό') in line):
			print(line.rstrip())