with open("norms_from_dict.out") as fileinst:
	for line in fileinst:
		if ("-α, -ο" in line):
			print(line.rstrip())