
from flask import Flask

app = Flask(__name__)   

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/bye")
def bye():
    return "Bye!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3500)   # 0.0.0.0: 모든 ip의 요청을 받겠다(모든 접근을 허용하겠다.)
                                         # port: port번호를 바꾼다