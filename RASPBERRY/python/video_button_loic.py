#!/usr/bin/env python

from time import sleep
import os
import sys
import RPi.GPIO as GPIO

import OSC
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

#---- OSC SERVER
receive_address = '192.168.1.2', 9111

s = OSC.ThreadingOSCServer(receive_address)
s.addDefaultHandlers()

allume = False

#---- FONCTION POUR AFFICHER LES MESSAGES PROVENANT D'OSC
def printing_handler(addr, tags, stuff, source):
#       print addr
        if addr == '/1/on':
                print "Test", stuff
                allume = True
                GPIO.output(18,True)
                os.system('omxplayer /home/pi/mp4/SYCLORAMA.mp4')
#       elif addr == '/ping':
#               print "PING"
        elif addr== '/1/off' :
                GPIO.output(18,False)
                os.system('killall omxplayer')


s.addMsgHandler("/1/on", printing_handler)
s.addMsgHandler("/1/off", printing_handler)

#---- FONCTION POUR LANCER LE SERVEUR OSC
def main():
        print ("Starting OSCServer")
        st = threading.Thread(target=s.serve_forever)
        st.start()

#---- ON LANCE LE SERVEUR
main()