
list1 = [1,2,3,4]

print(list1[0]) # 0번째 자리
print(list1[-1]) # 끝에서 첫번째

list2 = [5,6,7,8]
list3 = list1 + list2 # 리스트 더하기도 가능
print(list3)

list4 = [list1] + [list2]
print(list4)

# list2.append(9) 밑에 줄이랑 같다.
list2 = list2 + [9] # + 9는 타입이 달라서 안들어감
print(list2)


# 요소 제거
print('='*50)
arr = [5,6,7,8]

arr.remove(8) # 일치하는 데이터를 삭제
print(arr) #[5,6,7]

del arr[0] # 0번지 데이터 삭제
print(arr) #[6,7]

# 끝에 추가
print('='*50)
arr2 = [5,6,7,8]

arr2.append(9) # 끝에 9추가
print(arr2) #[5,6,7,8,9]

arr2 = arr2 + [10] # 타입을 같게 해줘야한다
print(arr2) #[5,6,7,8,9,10]

# 원하는 위치에 추가
print('='*50)
arr3 = [5,6,7,8]

arr3.insert(2, 500) # 2번지 자리에 500삽입
print(arr3) # [5,6,500,7,8]

# 정렬
print('='*50)
arr4 = [8,5,1,7,3]

arr4.sort() # 오름차순
print(arr4) # [1,3,5,7,8]

arr4.reverse() # 내림차순
print(arr4) # [8,7,5,3,1]

# 반복문
print('='*50)
arr5 = [1,3,5,7]

for i in arr5:
    print(i) # 4칸 들여쓰기(tab 1번)

for i in range(0, 6): # 0~5까지 6개 출력
    print(i) # 4칸 들여쓰기(tab 1번)







