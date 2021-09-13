import sys

# 이미 import된 모듈 (import를 따로 안해도 쓸수있음)
#print(sys.modules)

# 기본 내장 라이브러리
print(sys.path)

# from 뒤에는 파일명이나 폴더명
# import 뒤는 파일명이나 변수, 클래스, 함수
from http import server