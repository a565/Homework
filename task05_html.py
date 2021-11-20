'''
Скачать содержимое страницы https://epam.com с помощью requests
Посчитать количество тегов div на этой странице (лучше использовать для этого библиотеку beautifulsoup4)
'''
import requests

#GET запрос без параметров

response = requests.get('https://www.epam.com')
#response = requests.get('http://ya.ru')
#response.status_code
#response.status_code == requests.codes.ok

#response.headers
#response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')



sum=0
for link in soup.find_all('div'):
    sum = sum + 1
print(sum)

