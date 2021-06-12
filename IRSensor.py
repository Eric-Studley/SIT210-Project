import RPi.GPIO as GPIO 
import time
sensor = 40

def setup():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(sensor, GPIO.IN)
    print("IR Sensor Ready")

def sense():
    if GPIO.input(sensor):           
        print("Detected")
        return True
    else:
        print("Nothing Found")
        return False
            
            