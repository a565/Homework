'''
Создать класс в конструктор которого передается одно число
В этом классе дожен быть метод show, который распечатывает
переданное число.
'''

class First:
    "Определяет объект класса"
    cl = 1 # переменные для всех экземпляров класса

    def __init__(self, value): # конструктор
        # self – это экземпляр
        self.data = value

    def _setdata(self, value): # Определяет метод класса
        self.data = value

    def show(self):
        print(self.data)

'''
Создать класс, который наследуется от предыдущего класса и в этот
класс передается два числа.
Данный класс реализует метод calc, который складывает эти два числа.
'''
class Second(First):
    def __init__(self, value,value2 ):
        self.data2 = value2
        # Необходимо вызывать вручную если переопределили конструктор
        super().__init__(value)
        print(super())

    def show(self):
        super().show()
        print("The first atribute {}".format(self.data))

    def calc(self):
        sum = self.data + self.data2
        return sum


f1 = First(1)
f2 = First(22)

f1.data
f2.data

f1.show()
f2.show()

s1 = Second(3, 5)
s1.data2
s1.show()
s1.calc()

'''
Создать блок try/except/finally
Внутри блока try создать выражение, которое делит на 0.
Перехватить эту ошибку и распечатать сообщение пользвоателю.
'''
try:
#    raise SyntaxError("My syntax error")
    #Nones # NameError
#    1 + "2" # TypeError
    i=1/0 # ZeroDivisionError
    print("All fine")
except ZeroDivisionError:
    print("ZeroDivisionError")
finally: # Этот блок выполняется всегда.
    print ("In finally block")




'''
Создать декоратор, который перед запуском функции распечатывает все 
аргументы вызываемой функции.
'''

def trace(func):
    def inner(*args, **kwargs):
        print("Аргументы функции {} это {}".format(func.__name__, args, kwargs))
        return func(*args, **kwargs)  #исполняет функцию?
    return inner

@trace
def summa(x,y):
    return x+y

summa(10,11)

'''
Создать класс в котором применить декоартор  @property для доступа 
к внутренней переменной.
'''

class Decor:
    def __init__(self, value):
        self._data = value

    @property
    def data(self):
        return self._data #/ 2

    @data.setter # Для присваивания
    def data(self, v):
        self._data = v

d = Decor(23)
d.data
d.data=40
d.data

'''
Создать генератор который возвращает числа от 1 до 10
'''


def first_gen():
    a = 1
    n=11
    while a < n:
        yield a
        a += 1


for g in first_gen():
    print(g)
'''
С помощью стандартной функции collections.namedtuple создать объект для хранения точки 
в трехмерном пространстве.
'''
import collections
#collections.namedtuple
Point = collections.namedtuple('Point', ['x', 'y','z'])
p1 = Point(x=1, y=2, z=3)
p2 = Point(11, 22,33)
d=p1.x + p2.x
print (p1.z,d)

'''
Создать пакет в котором будет функция для распечатки текущей даты (можно использовать 
пакет datetime). Для данного пакета подготовить setup.py для установки.
'''

from datetime import date
current_date = date.today()
print(current_date)

import mypackage.work
mypackage.work.m_date()