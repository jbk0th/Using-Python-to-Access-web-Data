import re
fname = input('Enter a file name:\n')
fhand = open(fname)
num_list = list()
int_sum = 0
for line in fhand:
	line = line.rstrip()
	x = re.findall('([0-9]+)',line)
	if len(x) > 0:
		num_list = num_list + x 

for element in num_list:
	num = int(element)
	int_sum = int_sum + num
	
print(int_sum)