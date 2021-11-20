'''
С помощью SQL запросов создать таблицу содержаюую 2 стобца: номер и имя
Добавить три строки с данными.
Получить данные из таблицы и распечатать их на экране.
'''

import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE names
             (num, name)''')
c.execute("INSERT INTO names VALUES (3,'Piter')")
c.execute("INSERT INTO names VALUES (2,'Olga')")
c.execute("INSERT INTO names VALUES (1,'Denis')")
conn.commit()

for row in c.execute('SELECT * FROM names  ORDER BY num'):
        print(row)

conn.close()
