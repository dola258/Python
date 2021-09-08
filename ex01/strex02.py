
test = '가나-다-라'

print(test[:2])

print(test.find('-')) # 첫번째 -의 위치
print(test.find('-', 3)) # 3번째 자리부터 -의 위치
print(test.rfind('-')) # 오른쪽부터 첫번째 -의 위치

# 문제 1 : 끝번호 4자리 찾기
phone1 = '051-222-3333'
si1 = phone1.rfind('-') + 1

print(phone1[-4:])
print(phone1.rfind('-'))
print(phone1[si1:])

# 문제 2 : 가운데 번호 찾아내기
phone2 = '02-777-9999'

fi = phone2.find('-') + 1
li = phone2.rfind('-')
print(phone2[fi:li])

print(phone2[3:-5])