

from picamera import PiCamera
from time import sleep

def take_photo():
    camera = PiCamera()

    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    camera.close()
    print('Photo Taken')
    
