import Email
import Camera
import IRSensor
import Motion
import time
from datetime import datetime


print("Set up sensors")
Motion.setup()
IRSensor.setup()

try:
    while True:
        if Motion.sense():
            print("Motion Found")
            time.sleep(3)
            start_time = datetime.now()
            while IRSensor.sense():
                print("catto exists")
                time.sleep(5)
                   
            
            end_time = datetime.now()
            elapsed_seconds = (end_time - start_time).total_seconds()
            print(start_time)
            print(end_time)
            print(elapsed_seconds)
            
            if (elapsed_seconds > 10):
                print("takephoto")
                Camera.take_photo()
                
            
            time.sleep(3)
        else:
            print("False")
            time.sleep(3)
            
except KeyboardInterrupt:
    GPIO.cleanup()