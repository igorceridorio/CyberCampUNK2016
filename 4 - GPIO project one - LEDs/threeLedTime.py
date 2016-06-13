import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
while True:
	GPIO.output(4, True)
	time.sleep(1)
	GPIO.output(4, False)
	GPIO.output(17, True)
	time.sleep(1)
	GPIO.output(17, False)
	GPIO.output(22, True)
	time.sleep(1)
	GPIO.output(22, False)