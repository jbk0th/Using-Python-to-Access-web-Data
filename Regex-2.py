import re
fname = input('Enter a filename:')
fhand = open(fname)
num_list = 0
count = 0
for line in fhand:
	line = line.rstrip()
	y = re.findall('New Revision: ([0-9.]+)',line)
	if len(y) > 0:
		y = float(y[0])
		count = count + 1
		num_list = num_list + y
		
print(num_list/count)

