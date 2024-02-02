import threading #쓰레드 모듈을 사용하기 위해 import한다.
import time #시간 모듈을 사용하기 위해 import한다.

flag_exit = False #쓰레드 종료 플래그

def t1():
    while True:
        print("Thread 1")
        time.sleep(1)
        if flag_exit == True:
            break
        
thread = threading.Thread(target=t1) #쓰레드를 생성한다.
thread.start() #쓰레드를 시작한다.

try : 
    while True:
        print("Main Thread")
        time.sleep(1)
        
except KeyboardInterrupt:
    pass
flag_exit = True #쓰레드 종료 플래그를 설정한다.
thread.join() #쓰레드가 종료될때까지 대기한다.