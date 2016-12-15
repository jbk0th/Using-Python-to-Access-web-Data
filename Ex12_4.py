from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

for tag in tags:

	print('TAG:', tag)
	print('URL:', tag.get('href', None))
	print('Contents:', tag.contents[0])
	print('Attrs:', tag.attrs)