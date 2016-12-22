import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter URL: ')
num = input('Enter count: ')
count = 0
pos = input('Enter position: ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

while count < (int(num)):
	if count < 1:
		print ('Retrieving: ', url)
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	postag = tags[int(pos) -1]
	print('Retrieving: ',postag.get('href', None))
	url = postag.get('href', None)
	count = count + 1
	
