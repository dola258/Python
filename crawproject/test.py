from bs4 import BeautifulSoup
import news_title as new


soup = BeautifulSoup(str(new.oid_list), 'html.parser')

for title in soup:
    title_tag = soup.select_one(".pannel innerimg")

    print(title_tag)
