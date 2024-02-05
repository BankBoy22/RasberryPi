
from flask import Flask     # flask 모듈을 불러움​
import RPi.GPIO as GPIO     # GPIO 모듈을 불러움​

#핀 번호 설정
red = 4
green =5
blue = 6

# GPIO 핀 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 핀 번호 설정
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

app = Flask(__name__)       # Flask라는 이름의 객체 생성​

@app.route('/')             # 기본 주소​

def hello():                # 해당 주소에서 실행되는 함수 정의 (뷰함수)​

   return "Hello Flask!"    # 반드시 return이 있어야하며, 해당 값을 화면에 보여줌​

@app.route('/red_on')       # /red_on 주소​
def red_on():
   GPIO.output(red, True)   # LED 켜기
   return "red on"          # 해당 문자열을 화면에 보여줌​

@app.route('/green_on')     # /green_on 주소​
def green_on():
   GPIO.output(green, True)
   return "green on"

@app.route('/blue_on')      # /blue_on 주소​
def blue_on():
   GPIO.output(blue, True)
   return "blue on"

@app.route('/off')          # /off 주소​
def off():
   GPIO.output(red, False)
   GPIO.output(green, False)
   GPIO.output(blue, False)
   return "off"

@app.route('/clean')        # /clean 주소​
def clean():
   GPIO.cleanup()
   return "clean"

if __name__ == "__main__":  # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분​

   app.run(debug = True, port = 8000, host ='192.168.0.133')  

   # host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정​

   # 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능