import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	urladdress = input('Enter url - :\n')
	adsplit = urladdress.split('/')
	print(adsplit)

	host_name = adsplit[2]
	print(host_name) #----handling and splitting the entered url to pass correct socket connect info
	mysock.connect((host_name, 80))
	cmd = ('GET '+ urladdress +' HTTP/1.0\n\n').encode()
	print(cmd)
	mysock.send(cmd)
	while True:
		data = mysock.recv(512)
		if (len(data) < 1):
			break
		print(data[:3000].decode())
	mysock.close()
except:
	print('Invalid url, please enter another')
	
	
