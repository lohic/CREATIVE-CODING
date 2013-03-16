#!/usr/bin/env python

from time import sleep
import os
import sys
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

# declaration de variable

test = 0

while True:
        GPIO.output(18,False)

        while ( GPIO.input(23) == True):
                print "23 is hot ",test
                GPIO.output(18, True)
                #os.system('omxplayer /home/pi/mp4/SYCLORAMA.mp4')
                test += 1
        #else:
        #       sys.exit()
        #if ( GPIO.input(24) == True ):
        #       os.system('omxplayer yerba_buena.mp3')

        sleep(1);

