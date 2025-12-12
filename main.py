import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


web_page = requests.get(URL)
web_page_str = web_page.text
soup = BeautifulSoup(web_page_str, features="html.parser")
movies = soup.find_all(name="h3", class_="title")

movie_list = []
for movie in movies:
    movie_list.append(movie.text)

reversed_movie_list = movie_list[::-1]

for movie in reversed_movie_list:
    print(movie)
