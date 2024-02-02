# Description: DC 모터 제어 예제
from gpiozero import Motor # gpiozero 모듈에서 Motor 클래스를 임포트
from time import sleep # time 모듈에서 sleep 함수를 임포트

# 모터 핀 세팅
motorR = Motor(forward=12, backward=13)

# 속도 조절을 위한 0에서 1 사이의 값
speed = 0.7

# 3초 동안 전진
motorR.forward(speed)
sleep(3)

# 3초 동안 후진
motorR.backward(speed)
sleep(3)

# 모터 정지
motorR.stop()

# 좌회전을 위한 다른 모터 생성
motorL = Motor(forward=14, backward=15)

# 3초 동안 좌회전
motorL.forward(speed)
sleep(3)

# 3초 동안 우회전
motorL.backward(speed)
sleep(3)

# 좌회전 모터 정지
motorL.stop()
