#!/usr/bin/python3

import RPi.GPIO
import time

RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(2, RPi.GPIO.OUT)
pwm = RPi.GPIO.PWM(2,100)

start = 80
stop = 50

format_time = '%Y-%m-%d_%H:%M:%S'

fansRunning = False

while True:
	tempFile = open('/sys/class/thermal/thermal_zone0/temp')
	temp = int(tempFile.read()) / 1000
	now = time.strftime(format_time, time.localtime(time.time()))

	if temp > start and fansRunning == False:
		pwm.start(100)
		fansRunning = True
		print(now + ": " + str(temp) + " ℃ Start Fan ")
	if temp < stop and fansRunning == True:
		pwm.stop()
		fansRunning = False
		print(now + ": " + str(temp) + " ℃ Stop Fan")

	time.sleep(1)
