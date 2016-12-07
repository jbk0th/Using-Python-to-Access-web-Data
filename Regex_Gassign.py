fname = input('Enter a file name:\n')
fhand = open(fname)
for line in fhand:
	print(line)