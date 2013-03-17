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


# ** http://opensoundcontrol.org/implementation/python-simple-osc
# ** http://www.ixi-audio.net/content/body_backyard_python.html
# http://wiki.labomedia.org/index.php/Envoyer_et_recevoir_de_l'OSC_en_python
# https://trac.v2.nl/wiki/pyOSC
# http://www.brianhensley.net/2012/07/how-to-get-1080p-videos-running-on-my.html
# http://elinux.org/Omxplayer
# ** http://hertaville.com/2012/11/18/introduction-to-accessing-the-raspberry-pis-gpio-in-c/
# http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/
# http://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/code
# ** http://learn.adafruit.com/adafruit-pi-cobbler-kit/overview#
# ** http://niltoid.com/blog/raspberry-pi-arduino/
# http://www.vrplumber.com/py3d.py