with open("norms_from_dict.out") as fileinst:
	for line in fileinst:
		if ("-ια, -ιο" in line):
			print(line.rstrip())