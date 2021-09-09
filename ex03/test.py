# import 파일명
import hello as h
h.sayHello() # hello~~everyone
print(h.num) # 10

# from은 h.을 빼고 쓸수있다
# from hello import *도 가능
from hello import sayHello, num
sayHello() # hello~~everyone
print(num) # 10
