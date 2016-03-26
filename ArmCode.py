#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import arms_module

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

U = 1
D = 0
R = U
L = D

#InitPin,UpPin,DownPin
#time.sleep(timeinseconds) -> Same as arduino Delay(timeinms)
m1 = Motor(18, 15, 14)
m2 = Motor(11, 9, 10)
m3 = Motor(21, 20, 16)
m4 = Motor(13, 6, 5)
m5 = Motor(7, 25, 8)
# DOWN is close
# UP is open

