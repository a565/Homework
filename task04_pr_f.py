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
       print('Каталог {}'.format(catalogs[i]))
       i = i + 1
       continue  # Перейти в начало циклa

dir_pr(catalogs)
'''
    i = 0
    for i in catalogs:
        print(catalogs[i])
        i = i + 1
        
        len=Catalogs.length
   for i = 0 t
   while catalogs[i]:
           logging.debug(catalogs[i])
           print('Каталог {}'.format(catalogs[i]))
           i=i+1
'''