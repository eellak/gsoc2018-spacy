with open("norms_from_dict.out") as fileinst:
	for line in fileinst:
		if (not "-α, -ικο" in line):
			if (not ("-η, -ο" in line or ('-ή, -ό') in line or ('-ή, -ο') in line or ('-η, -ό') in line )):
				if (not "-ια, -ιο" in line):
					if (not "-α, -ο" in line):
						s=line.rstrip()
						first_word=s.split('→')[0].strip()
						second_word=s.split('→')[1].strip()
						print("\"{}\": \"{}\",".format(first_word,second_word))


with open("adj_norms_1_parsed.out") as fileinst:
	for line in fileinst:
		s=line.rstrip()
		first_word=s.split('→')[0].strip()
		second_word=s.split('→')[1].strip()
		print("\"{}\": \"{}\",".format(first_word,second_word))
with open("adj_norms_2_parsed.out") as fileinst:
	for line in fileinst:
		s=line.rstrip()
		first_word=s.split('→')[0].strip()
		second_word=s.split('→')[1].strip()
		print("\"{}\": \"{}\",".format(first_word,second_word))
with open("adj_norms_3_parsed.out") as fileinst:
	for line in fileinst:
		s=line.rstrip()
		first_word=s.split('→')[0].strip()
		second_word=s.split('→')[1].strip()
		print("\"{}\": \"{}\",".format(first_word,second_word))
with open("adj_norms_4_parsed.out") as fileinst:
	for line in fileinst:
		s=line.rstrip()
		first_word=s.split('→')[0].strip()
		second_word=s.split('→')[1].strip()
		print("\"{}\": \"{}\",".format(first_word,second_word))
