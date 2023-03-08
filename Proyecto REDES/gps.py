import serial
import pynmea2
import datetime
import time
import requests

SERIAL_PORT = "/dev/ttyUSB0"
running = True

def parseGPS(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        if msg.lat != 'None' and msg.lat != '':
               url = "http://192.168.1.48:4040/api/gps"
               payload = {'latitud': msg.lat, 'latitud_direccion': msg.lat_dir,'longitud': msg.lon, 'longitud_direccion': msg.lon_dir, 'altitud': msg.altitude, 'altitud_unidad': msg.altitude_units,'satelites': msg.num_sats, 'fecha': datetime.datetime.now()}
               print(payload)
               data = requests.post(url, payload)
               print(data)
               time.sleep(10)
               print("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s -- Satellites: %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units,msg.num_sats))
        else:
               print("Sin Conexión")

print("Application started!")
gps = serial.Serial(SERIAL_PORT, baudrate = 9600,timeout = 0.5)
W_buff= ["AT+CGNSPWR=1\r\n","AT+CGNSSEQ=\"RMC\"\r\n","AT+CGNSINF\r\n","AT+CGNSURC=2\r\n","AT+CGNSTST=1\r\n"]
gps.write(W_buff[0].encode())
gps.flushInput()
time.sleep(1)
gps.write(W_buff[1].encode())
time.sleep(1)
gps.write(W_buff[2].encode())
time.sleep(1)
gps.write(W_buff[3].encode())
time.sleep(1)
gps.write(W_buff[4].encode())

gps.flushInput()

while running:
    try:
        str = gps.readline()
        #print(str)
        parseGPS(str.decode())
    except KeyboardInterrupt:
        running = False
        #gps.reset_output_buffer()
        gps.close()
        print("Application closed!")
    except:
        # You should do some error handling here...
        print("Application error!")

