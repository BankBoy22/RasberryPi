from flask import Flask, render_template
import RPi.GPIO as GPIO

sw_pin_list = [14,15,18] # 스위치 핀 번호 리스트

GPIO.setmode(GPIO.BCM) # GPIO 핀 번호 모드 설정

for sw_pin in sw_pin_list:
    GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 스위치 핀을 입력으로 설정
    
app = Flask(__name__) # Flask라는 이름의 객체 생성

sw_state_list = [0,0,0] # 스위치 상태 리스트

@app.route('/') # 기본 주소
def home():
    for i in range(3):
        sw_state_list[i] = GPIO.input(sw_pin_list[i])
    return render_template('buttonState.html', sw_state_list=sw_state_list)

if __name__ == "__main__":  # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분​

   app.run(debug = True, port = 8000, host ='192.168.0.133')  

   # host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정​

   # 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능