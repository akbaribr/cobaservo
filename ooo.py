import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

servo1.start(0)

def gerak():
    time.sleep(5)
    servo1.ChangeDutyCycle(20)
    time.sleep(2)
    servo1.ChangeDutyCycle(2)
    time.sleep(2)
