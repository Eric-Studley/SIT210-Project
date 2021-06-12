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
        if IRSensor.sense():
            time.sleep(3)
            start_time = datetime.now()
            while IRSensor.sense():
                print("Max is still eating")
                time.sleep(5)
                
            end_time = datetime.now()
            elapsed_seconds = (end_time - start_time).total_seconds()
            print(start_time)
            print(end_time)
            print(elapsed_seconds)
            
            if (elapsed_seconds > 10):
                print("takephoto")
                Camera.take_photo()
                Email.send_email(end_time, str(elapsed_seconds))
            
            time.sleep(3)
        else:
            time.sleep(3)
            
except KeyboardInterrupt:
    GPIO.cleanup()
