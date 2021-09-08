
# if 조건:
#    실행
# else:
#    실행


isChecked = False

if isChecked:
    print("안녕")
else:
    print("굿바이")

print("="*80)

num = 10

if num>=10:
    print("만점")
elif num>5: # else if -> elif
    print("평균")
else:
    print("미만")

# or / and
if True or False:
    print("투루입니다")
if True and False:
    print("투루입니다")
else:
    print("투루도 아니고 펄스도 아니여")

# 아무것도 스택에 안적고 싶으면 pass
if True:
    pass

# 조건부 표현식
score = 80
# 한줄로 써야한다 / 성공이 앞, 실패가 뒤
# 스코어가 60초과면 success 아니면 fail
message = "success" if score>60 else "fail"
print(message)  









