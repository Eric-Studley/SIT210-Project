import RPi.GPIO as GPIO 
sensor = 38

def setup():
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(sensor, GPIO.IN)
    print("Motion Sensor Ready")

def sense():
    if GPIO.input(sensor):     
        return True
    else:
        return False
