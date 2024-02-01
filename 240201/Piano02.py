#버튼을 누르면 도레미파가 나오는 프로그램
import RPi.GPIO as GPIO
import time

#사용할 GPIO 핀의 번호를 설정
button_pin1 = 22
button_pin2 = 23
button_pin3 = 24
button_pin4 = 25
Buzzer_pin = 18
LED_RED = 4
LED_GREEN = 5
LED_BLUE = 6

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
# LED 핀을 출력으로 설정
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

#처음에는 LED의 핀을 모두 LOW로 설정
GPIO.output(LED_RED, 0)
GPIO.output(LED_GREEN, 0)
GPIO.output(LED_BLUE, 0)

#부저의 pwm을 설정
Buzzer = GPIO.PWM(Buzzer_pin, 100)

#모든 LED를 켜는 메소드
def turnOnAllLED():
    GPIO.output(LED_RED, 1)
    GPIO.output(LED_GREEN, 1)
    GPIO.output(LED_BLUE, 1)

#모든 LED를 끄는 메소드
def turnOffAllLED():
    GPIO.output(LED_RED, 0)
    GPIO.output(LED_GREEN, 0)
    GPIO.output(LED_BLUE, 0)

#무한반복
while True:
    #버튼이 눌러지면
    if GPIO.input(button_pin1) == GPIO.LOW:
        print("Button1 pressed")
        Buzzer.start(10)
        Buzzer.ChangeFrequency(262)
        GPIO.output(LED_RED, 1)
        time.sleep(0.3)
        Buzzer.stop()
        GPIO.output(LED_RED, 0)
    if GPIO.input(button_pin2) == GPIO.LOW:
        print("Button2 pressed")
        Buzzer.start(10)
        Buzzer.ChangeFrequency(294)
        GPIO.output(LED_GREEN, 1)
        time.sleep(0.3)
        Buzzer.stop()
        GPIO.output(LED_GREEN, 0)
    if GPIO.input(button_pin3) == GPIO.LOW:
        print("Button3 pressed")
        Buzzer.start(10)
        Buzzer.ChangeFrequency(330)
        GPIO.output(LED_BLUE, 1)
        time.sleep(0.3)
        Buzzer.stop()
        GPIO.output(LED_BLUE, 0)  
    if GPIO.input(button_pin4) == GPIO.LOW:
        print("Button4 pressed")
        Buzzer.start(10)
        Buzzer.ChangeFrequency(349)
        turnOnAllLED()
        time.sleep(0.3)
        Buzzer.stop()
        turnOffAllLED()
        
#GPIO 개방을 해준다.
GPIO.cleanup()




