from flask import Flask, request
import random

app = Flask(__name__)

pw = str(random.randint(3, 9))
print(f'\nGenerated password, {pw}\n')

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		with open('index.html', 'r') as f:
			data = f.read()
		return data
			
					
	elif request.method == 'POST':
		form_data 	= request.form.to_dict()

		if form_data:
			print(f'\nThe current password is {pw}.')
			print(f'POST {form_data}\n')
			
			if form_data['id'] != '' and form_data['pw'] == pw:
				return data

			else:
				with open('index_fail.html', 'r') as f:
					data = f.read()
				return data		

if __name__ == "__main__":
	app.run(port=8080, debug=True)