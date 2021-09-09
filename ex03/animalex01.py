# 상속
class Animal:
    def sound(self):
        print("동물소리")

# Animal을 상속받는다.
class Dog(Animal):
    def sound(self):          # 오버라이드(재정의)
        print("강아지 소리")

d = Dog()
d.sound() # 강아지소리

a = Animal()
a.sound() # 동물소리




