import RPi.GPIO as GPIO
import time
import requests
import datetime
from subprocess import call, run

ESPERA = 0.5
PIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.LOW)

run(['echo', '>','99866325', 'numeroSMS.txt'])
run(['echo', '>','Se ha desactivado el riego', 'numeroSMS.txt'])
run(['python3','/proyecto/sms.py'])
run(['python3','/proyecto/enviarCorreoApagado.py'])
payload = {'descripcion':"Se ha desactivado el riego", 'fecha': datetime.datetime.now()}
requests.post("http://192.168.1.48:4040/api/logs", payload)
