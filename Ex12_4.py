from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup("p")
	
print('The number of paragraphs on this page is', len(tags))