'''Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com.
Скачанную информацию надо сохранить в файл.'''

import requests

#GET запрос без параметров

response = requests.get('https://www.epam.com')


from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

f = open("epam-html.txt", "w", encoding="cp1251")   # "w" - создать файл для записи
print(soup.text, file=f)           # печать в файл
f.close()

fb = open("testw.txt", "wb")
fb.write(b'hello')
fb.write("Привет".encode("cp1251"))
fb.close()