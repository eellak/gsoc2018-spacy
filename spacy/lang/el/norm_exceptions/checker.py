new_lines=[]
prev_lines=[]
normal_lines=[]
with open('norms_method_1.txt') as fileinst:
	for line in fileinst:
		prev_lines.append(line)

with open('all.out') as fileinst2:
	for line in fileinst2:
		normal_lines.append(line)

for k in prev_lines:
	if (not (k in normal_lines) ):
		new_lines.append(k)
for m in new_lines:
	print(m.rstrip())

for m in normal_lines:
	print(m.rstrip())
