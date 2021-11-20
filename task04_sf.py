'''Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com.
Скачанную информацию надо сохранить в файл.'''

import requests

#GET запрос без параметров

response = requests.get('https://www.epam.com')


from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

f = open("epam-html.txt", "w")  # "w" - создать файл для записи
f.write(soup)              # записать в file-подобный объект
f.close()