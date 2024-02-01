import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)#LED(RED)
GPIO.setup(27, GPIO.IN)#센서

try:
    while True:
        pir_state = GPIO.input(27) #센서 상태 저장
        if pir_state == 1:
            GPIO.output(4, 1)
            print("Motion Detected")
            time.sleep(0.5)
        else:
            GPIO.output(4, 0)
            print("No Motion")
            time.sleep(0.5)

#Ctrl+C를 누르면 종료(try-except 구문 사용)  
except KeyboardInterrupt:
    GPIO.cleanup()