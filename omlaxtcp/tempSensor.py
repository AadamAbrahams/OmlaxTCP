import pigpio
import smbus2
import time
import crcmod.predefined
import TCP

scanned = False
init = False

def setup(channel, omAddress, arraysize):
	global BUFFER_LENGTH
	global tdata_raw
	global handle
	global tdata
	global pi
	BUFFER_LENGTH =  (arraysize *2 ) + 3
	pi = pigpio.pi()
	piGPIO = pi.get_pigpio_version()
	bus = smbus2.SMBus(channel)
	time.sleep(0.1)
	handle = pi.i2c_open(channel, omAddress)
	tdata_raw = [0]*BUFFER_LENGTH
	tdata = [0.0]*arraysize

def feverScanner():
	global init
	global scanned
	tempReading()
	if (tdata[0] > roomtemp) and (tdata[0] > 30):
		if (init == False):
			init = True
			feverScanner()
		else:
			init = False
			scanned = True
			TCP.client(str(tdata[0]))
			if (tdata[0]) > 38:
                                scanned = False
				time.sleep(1)
				
def tempReading():
        global tdata
        time.sleep(1)
  	(bytes_read, tdata_raw) = pi.i2c_read_device(handle, BUFFER_LENGTH)
   	a = 0
   	b = len(tdata_raw)-2
   	for i in range(2,b,2):
      		tdata[a]=float((tdata_raw[i+1]<<8) | tdata_raw[i])/10
      		a += 1

def roomtemp():
        global roomtemp
        tPAT = float((tdata_raw[1]<<8)|tdata_raw[0])/10
   	roomtemp = tPAT
   	
def roomtempValue():
        return(roomtemp)

def tempReadingValue():
        return(tdata[0])
