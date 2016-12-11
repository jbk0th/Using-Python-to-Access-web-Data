import re
fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	#if re.search('From:',line):
	#if re.search('^From:', line):
	#if re.search('^From:.+@', line):
	#x = re.findall('\S+@\S+', line:
	#x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-z]', line)
	#x = re.findall('^X-\S*: [0-9.]+', line)
	#x = re.findall('^X-\S*: ([0-9.]+)', line)
	#x = re.findall('^Details:.*rev=([0-9.]+)',line)
	x = re.findall('^From .* ([0-9][0-9]):', line)
	if len(x) > 0:
		print(x)
		
