
from flask import Flask, render_template, url_for, redirect     # flask 모듈을 불러움​
import RPi.GPIO as GPIO     # GPIO 모듈을 불러움​

#핀 번호 설정
led_pin_dict = {'red': 4, 'green': 5, 'blue': 6} # 딕셔너리로 핀 번호 설정

# GPIO 핀 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 핀 번호 설정
for pin in led_pin_dict.values():
    GPIO.setup(pin, GPIO.OUT)
    
led_stat_dict = {'red': False, 'green': False, 'blue': False} # 딕셔너리로 LED 상태 설정

app = Flask(__name__)       # Flask라는 이름의 객체 생성​

@app.route('/')             # 기본 주소​

def home():                # 해당 주소에서 실행되는 함수 정의 (뷰함수)​
   return render_template('ledControll.html', led_stat_dict=led_stat_dict)    # home.html을 렌더링하여 보여줌

@app.route('/<color>/<int:stat>')       # /red_on 주소​
def led_control(color, stat):
    led_stat_dict[color] = state 
    GPIO.output(led_pin_dict['red'], led_stat_dict['red'])
    GPIO.output(led_pin_dict['green'], led_stat_dict['green'])
    GPIO.output(led_pin_dict['blue'], led_stat_dict['blue'])
    
    #LED 현황을 적용하여 LED를 실제로 켜고 끔
    return redirect(url_for('home'))
 
#모든 LED를 한번에 제어하는 주소
@app.route('/all/<int:stat>')
def all_led_control(stat):
    for color in led_stat_dict.keys():
        led_stat_dict[color] = bool(stat)
        GPIO.output(led_pin_dict[color], led_stat_dict[color])
    return redirect(url_for('home'))
 
if __name__ == "__main__":  # 웹사이트를 호스팅하여 접속자에게 보여주기 위한 부분​

   app.run(debug = True, port = 8000, host ='192.168.0.133')  

   # host는 현재 라즈베리파이의 내부 IP, port는 임의로 설정​

   # 해당 내부 IP와 port를 포트포워딩 해두면 외부에서도 접속가능