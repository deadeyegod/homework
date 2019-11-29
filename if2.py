"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def string_reader(string1,string2):
    str(string1)
    str(string2)
    if string1 == string2:
        return 1
    elif string1 != string2 and len(string1) > len(string2) and string2 != 'learn':
        return 2 
    elif string1 != string2 and string2 =='learn':
        return 3

string1 = str(input("write the first string\n"))
string2 = str(input('write the second string\n'))
print(str(string_reader(string1,string2)))
