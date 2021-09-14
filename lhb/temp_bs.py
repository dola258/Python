from bs4 import BeautifulSoup
import movie_api as movie

soup = BeautifulSoup(movie.callTempApi(), 'html.parser')

def temp():
    temp_tag = soup.select_one("#wrap #container .info_temperature .todaytemp")
    temp = temp_tag.text
    
    return temp
