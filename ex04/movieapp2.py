# 20개의 영화 데이터의 제목, 평점, 러닝시간, 미디엄-커버-이미지
# for(반복문)을 돌려서 Console에 이쁘게 출력하시오
# 구분(===============================)

# ex
# 제목:~~~~
# 평점:~~~~
# 러닝시간:~~~~
# 사진:~~~~(url)
# =====================================================

import requests

url = '''
    https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=20
'''
response = requests.get(url)

responseDict = response.json() # 딕셔너리 타입으로 변환
movies = responseDict["data"]["movies"]

for movie in movies:
    
    print(f"제목: {movie['title']}") # $"":  +없이 한줄의 str로 나온다
    print(f"평점: {str(movie['rating'])}점") # $"": +없이 한줄의 str로 나온다
    print("러닝시간: " + str(movie["runtime"]) + "분")
    print("사진: " + movie["medium_cover_image"])
    print("="*50)