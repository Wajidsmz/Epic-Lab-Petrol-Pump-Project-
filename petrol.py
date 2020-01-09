import csv
import os
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import datetime
from datetime import datetime


data1=['sensor_id,date,time']
with open ('/home/pi/Desktop/Project/data.csv','a') as f:
    writer=csv.writer(f)
    writer.writerow(data1)
    print(data1)


    def button_callback(channel):
	
        
        if(GPIO.input(channel)==GPIO.HIGH):
	    data_time=datetime.utcnow().isoformat()
            data=['sensor1',data_time]
            print(data)
            with open ('/home/pi/Desktop/Project/data.csv', 'a') as f:
                print ('file open')
                writer=csv.writer(f)
	        writer.writerow(data)
                
        
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    print ('setup')
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    print ('setup Done')
    GPIO.add_event_detect(8,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
   
    #message = input("Press enter to quit\n\n") # Run until someone presses enter

    def button_callback(channel):
        if(GPIO.input(channel)==GPIO.HIGH):
	    data_time=datetime.utcnow().isoformat()
            data=['sensor2',data_time]
            print(data)
            with open ('/home/pi/Desktop/Project/data.csv', 'a') as f:
                writer=csv.writer(f)
                writer.writerow(data)
        
        
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
    #message = input("Press enter to quit\n\n") # Run until someone presses enter


    def button_callback(channel):
        if(GPIO.input(channel)==GPIO.HIGH):
	    data_time=datetime.utcnow().isoformat()
            data=['sensor3',data_time]
            print(data)
            with open ('/home/pi/Desktop/Project/data.csv', 'a') as f:
                writer=csv.writer(f)
                writer.writerow(data)
        
        
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.add_event_detect(12,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
