# 모든 언어는 class는 메모리에 띄울려면 new로 heap에 올려야한다
class User:
    username="ssar"
    password="1234"

# 8번 라인에서 heap으로 User클래스가 메모리에 뜬다
# return 타입을 몰라도 된다.
u = User() 

print(u.username) # ssar