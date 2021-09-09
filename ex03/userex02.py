# self를 하는 순간 전역변수로 선언한 것과 같다.

class User:
    
    # 생성자의 self는 객체 생성시 자동 주입된다.
    # __init__함수가 생성자이다.
    def __init__(self, username, password="1234"):
        self.username = username
        self.password = password

u = User("ssar", "1234")  
u1 = User("cos")

print(u.username)  # ssar
print(u1.username) # cos

print("="*80)

print(u.__dict__)  # 클래스를 딕셔너리 타입으로 변경해준다.
                   # 외부로 통신할때 클래스를 딕셔너리 타입으로 변경해서 던지면 json이랑 똑같아서 보낼수 있다.

