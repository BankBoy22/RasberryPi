from flask import Flask, render_template #플라스크 모듈 호출

app = Flask(__name__) #플라스크 앱 생성

@app.route('/') #기본(루트) 경로
def hello():
    return render_template('index.html') #인덱스 페이지 출력

@app.route('/<username>') #username 경로
def hello_user(username):
    return render_template('index.html', user = username)

@app.route('/about') #about 경로
def about():
    return 'About page' #어바웃 페이지 출력
@app.route('/contact') #contact 경로
def contact():
    return 'Contact page' #컨택트 페이지 출력

if __name__ == '__main__': # 웹 서버 실행
    #debug의 의미는 코드가 수정되면 자동으로 재시작하겠다는 의미, port는 8000번으로 설정, host는 컴퓨터의 ip주소로 설정
    app.run(debug = True, port = 8000, host ='192.168.0.133')  