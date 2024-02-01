import RPi.GPIO as GPIO
import time

#사용할 GPIO 핀의 번호를 설정
button_pin1 = 22
button_pin2 = 23
button_pin3 = 24
button_pin4 = 25
Buzzer_pin = 18 

#setwarnings(False)로 경고 메시지를 제거
GPIO.setwarnings(False)
#GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)
#버튼 핀의 INPUT설정
GPIO.setup(button_pin1, GPIO.IN)
GPIO.setup(button_pin2, GPIO.IN)
GPIO.setup(button_pin3, GPIO.IN)
GPIO.setup(button_pin4, GPIO.IN)
#부저의 핀을 출력으로 설정
GPIO.setup(Buzzer_pin, GPIO.OUT)

#무한반복
while True:
    #버튼이 눌러지면
    if GPIO.input(button_pin1) == GPIO.LOW:
        print("Button1 pressed")
        GPIO.output(Buzzer_pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(Buzzer_pin, GPIO.LOW)
    if GPIO.input(button_pin2) == GPIO.LOW:
        print("Button2 pressed")
        GPIO.output(Buzzer_pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(Buzzer_pin, GPIO.LOW)
    if GPIO.input(button_pin3) == GPIO.LOW:
        print("Button3 pressed")
        GPIO.output(Buzzer_pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(Buzzer_pin, GPIO.LOW)
    if GPIO.input(button_pin4) == GPIO.LOW:
        print("Button4 pressed")
        GPIO.output(Buzzer_pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(Buzzer_pin, GPIO.LOW)
        
#GPIO 개방을 해준다.
GPIO.cleanup()

