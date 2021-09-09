# 예외 처리
# 예외는 항상 런타임시에 일어난다(미리 일어나는건 예외가 아님, 실행시 예상하지 못했던 에러)

try:
    print(2/1)
except Exception as e: # catch 대신 except 사용
    print(e)           # division by zero (0으로 나눌수 없다)    
finally:               # finally는 무조건 실행
    print("끝")

# 2.0
# 끝