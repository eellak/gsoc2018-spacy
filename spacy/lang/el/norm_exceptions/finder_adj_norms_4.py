with open("norms_from_dict.out") as fileinst:
	for line in fileinst:
		if ("-α, -ικο" in line):
			print(line.rstrip())