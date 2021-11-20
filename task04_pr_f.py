'''
2. Написать функцию, которая распечатает все файлы в каталоге. В функцию добавить вывод отладочной
информации через библиотеку logging (указать какой каталог обрабатывается и сколько файлов в каталоге
было распечатано).
'''
import subprocess
output = subprocess.run(["dir"], stdout=subprocess.PIPE)
print(output.stdout.decode())

import subprocess
#subprocess.run(["notepad"]) # windows
#output = subprocess.run(["ipconfig"], stdout=subprocess.PIPE) # windows
output = subprocess.run(["ipconfig", "/all"], stdout=subprocess.PIPE)
print(output)
print(output.stdout.decode())

import logging
"""
настройка корневого логгера 

отправка сообщений stderr
"""
logging.basicConfig(level=logging.DEBUG)
"""
отправка сообщений в stdout
"""
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
"""
отправка сообщений в файл
"""
logging.basicConfig(filename="info.log", level=logging.DEBUG)
logging.warning("My message")
logging.debug("That's it, beautiful and simple logging!")
