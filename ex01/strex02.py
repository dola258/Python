
test = '가나-다-라'

print(test[:2]) # 가나: 0번째 자리부터 2번째 자리 앞까지

print(test.find('-'))    # 2: 첫번째 -의 위치
print(test.find('-', 3)) # 4: 3번째 자리 이후부터 첫번째 -의 위치
print(test.rfind('-'))   # 4: 오른쪽부터 첫번째 -의 위치

# 문제 1 : 끝번호 4자리 찾기
phone1 = '051-222-3333'
si1 = phone1.rfind('-') + 1 # 8

print(phone1[-4:])       # 3333: 오른쪽부터 4자리
print(phone1.rfind('-')) # 7:    오른쪽부터 첫번째 -의 위치
print(phone1[si1:])      # 3333: 8(오른쪽부터 첫번째 -의 다음 위치)번 자리부터 끝까지 

# 문제 2 : 가운데 번호 찾아내기
phone2 = '02-777-9999'

fi = phone2.find('-') + 1 # 3: 왼쪽부터 첫번째 -의 다음 위치
li = phone2.rfind('-')    # 7: 오른쪽부터 첫번째 -의 위치

print(phone2[fi:li]) # 777: 3번째 자리부터 7번째 자리 전까지 
print(phone2[3:-5])  # 777: 3번째 자리부터 오른쪽으로 5번째자리 전까지