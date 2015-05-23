#!/usr/bin/python
from Radio import Radio
import RPi.GPIO as GPIO
import time

# callback function for pin 4, changing station
def changeStation(channel):
        global inOn
        if isOn == True:
                print "changing station..."
                GPIO.output(17,1)
                r.nextStation()
                time.sleep(0.5)
                GPIO.output(17,0)
        else:
                print "radio off, no change station"
                time.sleep(0.5)

def radioOnOff(channel):
        global isOn
        #print "isOn",isOn
        if isOn == True:
                print "radio off..."
                GPIO.output(11,0)
                r.stopStation()
                isOn = False
        else:
                print "radio on..."
                GPIO.output(11,1)
                r.startStation(1)
                isOn = True
# starts script
print "starts radio..."
r = Radio()
r.readStations()
isOn = False

# setting up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # change station
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP) # on/off
GPIO.setup(17,GPIO.OUT) # yellow led
GPIO.setup(11,GPIO.OUT) # green led

# adding a callback thread
GPIO.add_event_detect(4, GPIO.FALLING, callback=changeStation,bouncetime=300)
GPIO.add_event_detect(9, GPIO.FALLING, callback=radioOnOff,bouncetime=300)
while True:
        time.sleep(60)
        #GPIO.cleanup()
        #quit()

