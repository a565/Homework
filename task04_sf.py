'''Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com.
Скачанную информацию надо сохранить в файл.'''

import requests

#GET запрос без параметров

#response = requests.get('https://www.epam.com')
response = requests.get('http://localhost:5000/swagger/index.html')



f = open("local-html.txt", "wb")
f.write(response.text.encode("utf-8"))
f.close()

