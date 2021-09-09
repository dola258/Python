import requests

url = '''
    https://yts.mx/api/v2/list_movies.json?sort_by=rating&page_number=1&limit=2
'''
response = requests.get(url)

print(response.status_code)
#print(response.text)
print("="*80)
#print(response.content)

responseDict = response.json() # 딕셔너리 타입으로 변환
print(type(responseDict))
print(responseDict["status"]) # 딕셔너리에서 찾을때는 [""]으로 찾는다

movies = responseDict["data"]["movies"]
print(type(movies))

movie1 = movies[0]
movie1Title = movie1["title"]   # Doctor Who The Day of the Doctor
movie1Rating = movie1["rating"] # 9.4

print(movie1Title)
print(movie1Rating)





