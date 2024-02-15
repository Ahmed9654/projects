from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find_all(name='h3', class_='title')
with open('best 100 movie list', 'a', encoding='utf-8') as file:
    file.write('from best to worst\n')
    for i in title[::-1]:
        file.write(f'{i.get_text()}\n')

