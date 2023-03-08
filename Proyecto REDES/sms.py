import serial
import time

f = open ('/proyecto/numeroSMS.txt','r')
numero=f.read()

f = open ('/proyecto/dataSMS.txt','r')
mensaje=f.read()

port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)

port.write(b'AT\r')
port.flushInput()
rcv = port.readline()
print(rcv)
time.sleep(1)

port.write(b"AT+CMGF=1\r")
print("Text Mode Enabled…")
time.sleep(3)

concat = str("AT+CMGS=\""+ str(numero).strip() +"\"\r")
port.write(concat.encode())
msg = str(mensaje).strip()
print("sending message")
time.sleep(3)
port.reset_output_buffer()
time.sleep(1)
port.write(str.encode(msg+chr(26)))
time.sleep(3)
print("message sent…")
