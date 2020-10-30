import RPi.GPIO as GPIO
import time
import TCP
import tempSensor

def setup(motion):
        GPIO.setmode(GPIO.BCM)
	GPIO.setup(motion, GPIO.IN)

def motion_detect(motion):
	if (GPIO.input(motion) == 1):
		print "Motion detected"
	else:
		print "No motion detected"

def direc_detect(motion_out, motion_in):
	if (GPIO.input(motion_out) == 1):
		init_trig(motion_in)
		ensure_low(motion_out, motion_in)

	if (GPIO.input(motion_in) == 1):
		init_trig(motion_out)
		ensure_low(motion_out, motion_in)

def init_trig(motion):
	for x in range(40):
		time.sleep(0.1)
		if (GPIO.input(motion) == 1):
			if (motion == 1) and (tempSensor.scanned == False):
				GPIO.setup(4, GPIO.OUT)
				GPIO.output(4, GPIO.HIGH)
				time.sleep(2)
				GPIO.output(4, GPIO.LOW)
				print("BUZZ")
				break
			else:
				TCP.client(str(motion))
				tempSensor.scanned = False
				break

def speed_detect(motion_out, motion_in, distance):
		if (GPIO.input(motion_out) == 1):
			speed(timing(motion_in), distance)
			ensure_low(motion_out, motion_in)

		if (GPIO.input(motion_in) == 1):
			speed(timing(motion_out), distance)
			ensure_low(motion_out, motion_in)

def timing(motion):
	tic = time.perf_counter()
	while (GPIO.input(motion) != 1):
		pass

	toc = time.perf_counter()
	return tic - toc

def speed(time, distance):
	speed = distance/time
	TCP.client(str(speed))

def ensure_low(motion_out, motion_in):
	while (GPIO.input(motion_out) == 1) or (GPIO.input(motion_in) == 1):
		time.sleep(0.1)
