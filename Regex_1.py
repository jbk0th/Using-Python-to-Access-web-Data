import re
ifin = input('Enter file name:')
fname = open(ifin)
regex = input('Input a regular expression to match:\n')
ilist = list()
for line in fname:
	line = line.rstrip()
	y = re.findall(regex,line)
	if len(y) > 0:
		ilist = ilist + y
print(ifin,'had',len(ilist),'lines that matched', regex )
