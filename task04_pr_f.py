'''
2. Написать функцию, которая распечатает все файлы в каталоге. В функцию добавить вывод отладочной
информации через библиотеку logging (указать какой каталог обрабатывается и сколько файлов в каталоге
было распечатано).
'''

import os
catalogs=os.listdir(path='C:\Git\Pyton\Homework\mypackage')


def dir_pr(catalogs):
   import logging
   import sys

   logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
   len1 = len(catalogs)
   i=0

   while len1-i > 1:
       logging.debug(catalogs[i])
       #print('Каталог {}'.format(catalogs[i]))
       i = i + 1
       continue  # Перейти в начало циклa
   print(f'В каталоге было распечатано {i} файлов')
#print(f'Произведение {n} на {m} равно {prod}')


dir_pr(catalogs)


