"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


  
def age(ge):
    
    if ge <= 4:
        return 'sleep'
    elif 4 < ge <= 16:
        return 'go to school'
    elif 16 < ge <= 25:
        return 'go to university'
    elif 25 <= ge:
        return 'get a job'
    else:
        return 'die'

ge = int(input('What is your age?\n'))     
smt = age(ge)
print(str(smt))


