import re
fname = input('Enter a file name:\n')
fhand = open(fname)
num_list = list()
y = re.findall('([0-9]+)',fhand.read())
for number in y : 
	num_list.append(int(number))
print(sum(num_list))
