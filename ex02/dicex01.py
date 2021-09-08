# 딕셔너리 (사전)
# { "key": value } 딕셔너리
# { key : value } 자바스크립트 오브젝트
# { "key" : value } JSON

dic1 = { "username" : "ssar", "password":"1234", "age":19 }
print(type(dic1)) # dict

print(dic1["password"]) # 1234
print("="*50)

users = [
    { "username" : "ssar", "password":"1234", "age":19 },
    { "username" : "cos", "password":"1234", "age":30 }
]
print(users)
print(type(users)) # list

print(users[1]["age"]) # 1번 자리에 있는 age

for user in users:
    print(user["username"])

