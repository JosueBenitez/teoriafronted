import requests
import datetime

url = "http://192.168.1.48:4040/api/temperaturas"
payload = {'temperatura': 10, 'humedad': 50, 'fecha': datetime.datetime.now()}
data = requests.post(url, payload)
if data.status_code == 200:
	data = data.json()
	print(data)
