"""
## Запуск кода

- из консоли
- Из редакторов
- из IDE

C Python поставляется простой редактор [**IDLE**.](https://docs.python.org/3/library/idle.html)

Дзен питона
"""
import this


"""
### Функции помощи

Встроенная помощь
функция [help](https://docs.python.org/3/library/functions.html#help)
"""
help(help)

"""
В Python все есть объекты

### Список методов класса

функция [dir](https://docs.python.org/3/library/functions.html#dir)
"""
dir(int)
dir(1)

i = 1025
i.bit_length()

"""
### Узнать тип объекта

функция [type](https://docs.python.org/3/library/functions.html#type)
"""
type(1)
type('hello')
type(type)

# Простой пример программы
# Рассчет чисел Фиббоначи 2
n = 10
a = 0
b = 1
f = [a]
for i in range(n):
    temp = a
    a = b
    b += temp
    f.append(a)
print("Fibonacci number for {} is {}".format(n, a))
