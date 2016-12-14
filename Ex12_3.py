import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

doc_words = ''
num_char = 0
counts = dict()
for line in fhand:
	line = line.decode().strip()
	num_char = num_char + len(line)
	doc_words = doc_words + line
	
	# words = line.decode().strip()
	# for word in words:
		# counts[word] = counts.get(word,0) + 1
print(doc_words[:300])
print(num_char)