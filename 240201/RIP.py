#센서가 감지되면 Detected, 감지되지 않으면 Not detected를 출력하는 프로그램을 작성하시오.
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN)

while True:
    if GPIO.input(27):
        print("Detected")
    else:
        print("Not detected")
    time.sleep(0.5)
    
GPIO.cleanup()
    