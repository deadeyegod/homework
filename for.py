"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school =[{'school_class': '4a', 'scores':[3,4,4,5,2]},
    {'school_class': '4b', 'scores':[5,4,4,4,3]},
   {'school_class': '4c', 'scores':[2,2,3,3,3]}]
sum_of_grades = 0
quantity_of_students = 0
for class_ in school:
    sum_of_class_grades = 0
    for scores in class_['scores']:
        sum_of_grades += scores
        sum_of_class_grades += scores
    quantity_of_students += len(class_['scores'])
    average_class_score = f'Average grade for class {class_["school_class"]} is {sum_of_class_grades /len(class_["scores"])}'
   
    print(average_class_score)
average_grade_for_school = f'Average grade for school is {sum_of_grades / quantity_of_students}'

print(average_grade_for_school)    


    

