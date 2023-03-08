#!/usr/bin/python3
import sys
import Adafruit_DHT
import datetime
import requests
import time

while True:
	humidity, temperature = Adafruit_DHT.read_retry(11, 26)
	#print("{0}".format(temperature))
	url = "http://192.168.1.48:4040/api/temperaturas"
	payload = {'temperatura': temperature, 'humedad': humidity, 'fecha': datetime.datetime.now()}
	print(payload)
	data = requests.post(url, payload)
	time.sleep(1)
