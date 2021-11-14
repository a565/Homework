#### [Списки List]
spis1 = [1, 2, 'string1']
l1= spis1[0]
l2= spis1[1]
l3= spis1[2]
print(l1, l2, l3)

#### [Словари Dictonary]
dict = {'one': 1, 'two': 2, 'three': 3}
print (dict)
print (list(dict))
dict['one'] = 42
print(dict['one'])
print (dict)

#### [Множества Set]
set1 = {1, 2, 3}
print (set1)

#### [If ]
a=33
b=1
if a == 1 or b == 2:
    print(1)
elif a == 2:
    print(2)
elif a == 33:
    print(33)
else:
    print(3)
    print(5)

print(4)

#### [while]
a=10
while a > 1:
    a = a - 1
    if a % 2:
        print(a)
        continue  # Перейти в начало циклa
print(a, 'не в цикле')

'''
* Создать список из трех элементов и распечать его элементы
с помощью цикла for
'''
spis2 = [1, 2, '33']
for i in range(3):
    print(spis2[i])

#### распечатать числа от 0 до 5
for i in range(6):
    print(i)

#### создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass'

t_string = 'TEST'
if 'E' in t_string:
     print('pass')
else:
    print('fail')

#### Запросить данные у пользователя и распечатать их используя  форматированную строку.
print('Введите текст')
text1 = input('Текст: ')
print("Было введен текст: {} ".format(text1))

#### Распечатать содержимое файла.
f = open("test.txt", "w")  # "w" - создать файл для записи
f.write("Тест\n")              # записать в file-подобный объект
f.write("проверка")
f.close()

for line in open("test.txt"):
   print(line.strip())

print("конец файла")

###Создать функцию, которая принимает два аргумента, вернуть сумму двух аргументов.

def sum1(a,b):
    res=a+b
    return res
a=1
b=10
c=sum1(a,b)
print('Сумма равна {}'.format(c))

##Создать функцию которая принимает любое количество параметров, распечаатать эти параметры .
def fun2(x, y, *args):
    print(x, y, args)

fun2(1,2,3)
fun2(1,2,'test','test2')