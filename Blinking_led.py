import RPi.GPIO as GPIO
import time

Led_red = 21
Led_yellow = 22
Led_green = 23
Led_blue = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(Led_red, GPIO.OUT)
GPIO.setup(Led_yellow, GPIO.OUT)
GPIO.setup(Led_green, GPIO.OUT)
GPIO.setup(Led_blue, GPIO.OUT)


while True:
 GPIO.output(Led_red, GPIO.HIGH)
 GPIO.output(Led_yellow, GPIO.HIGH)
 GPIO.output(Led_green, GPIO.HIGH)
 GPIO.output(Led_blue, GPIO.HIGH)
 print("On")
 time.sleep(1)
 GPIO.output(Led_red, GPIO.LOW)
 GPIO.output(Led_yellow, GPIO.LOW)
 GPIO.output(Led_green, GPIO.LOW)
 GPIO.output(Led_blue, GPIO.LOW)
 print("Off")
 time.sleep(1)



