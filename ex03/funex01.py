# Python은 오버로딩이 안된다!
# def 함수선언
def add(n1, n2):
    return n1+n2

print(add(1,3)) # 4

# 선택적 매개변수↓
def minus(n1, n2=5): # 매개변수가 없으면 deFault값(5)
    return n1-n2

print(minus(10)) # 5
print(minus(10, 9)) # 1

# 1급 객체 : 함수같은거에 포함되지 않는다
sum = 20

def vartest():
    sum = 10 
    print(sum) # 함수안에 sum

vartest()

print("="*80)

sum2 = 20

def vartest2():
    global sum2 # 전역변수 sum을 사용하려면 global
    sum2 = sum2+1

vartest2()
print(sum2)