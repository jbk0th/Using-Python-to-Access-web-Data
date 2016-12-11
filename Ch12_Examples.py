# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)

# while True:
	# data = mysock.recv(512)
	# if (len(data) < 1):
		# break
	# print(data.decode())
# mysock.close()

# import socket
# import time

# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST,PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover.jpg HTTP/1.0\n\n')
# count = 0
# picture = b""

# while True:
	# data = mysock.recv(5120)
	# if (len(data) < 1): break
	# time.sleep(0.25)
	# count = count + len(data)
	# print(len(data), count)
	# picture = picture + data
	
# mysock.close()

# # Look for the end of the header (2CRLF)
# pos = picture.find(b"\r\n\r\n")
# print('Header Length',pos)
# print(picture[:pos].decode())

# #Skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open("stuff.jpg", "wb")
# fhand.write(picture)
# fhand.close()

# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
	# words = line.decode().split()
	# for word in words:
		# counts[word] = counts.get(word,0) + 1
# print(counts)

# import urllib.request, urllib.parse, urllib.error
# import re


# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# links = re.findall(b'href="(http://.*?)"', html)
# for link in links:
	# print(link.decode())
	
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# #Retrieve all  of the anchor tags

# tags = soup('a')
# for tag in tags:
	# print(tag.get('href',None))
	
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

# url = input('Enter - ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')

# #Retrieve all  of the anchor tags

# tags = soup('a')
# for tag in tags:
	# print('TAG:', tag)
	# print('URL:',tag.get('href',None))
	# print('Contents:', tag.contents[0])
	# print('Attrs:', tag.attrs)
	
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover.jpg')
fhand = open('cover.jpg', 'wb')
size = 0
while True:
	info = img.read(100000)
	if len(info) < 1: break
	size = size + len(info)
	fhand.write(info)
	
print(size, 'characters copied')
fhand.close()
	
