import time
import serial
import os, time
f = open ('/proyecto/numero.txt','r')
numero=f.read()
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.reset_input_buffer()
W_buf_logoin = "AT+GREG?\r\n"
W_buf_phone = "ATD" + str(numero).strip() + ";\r\n"
ser.write(str(W_buf_logoin).encode())
time.sleep(3)
ser.write(str(W_buf_phone).encode())
