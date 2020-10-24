#1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.write(line + '\n')
    line = input('Введите текст \n')
    if not line:
        break
my_f.close()

#2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.

my_file = open('file_1.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')

my_file = open('file_1.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')

my_file = open('file_1.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('file_1.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#Выполнить подсчет средней величины дохода сотрудников.

firm = {'Ivanov': 30000, 'Smirov': 15000, 'Sidorov': 40000, 'Petrov': 5000}
try:
    file_obj = open("file_1.txt", 'w')
    for last_name, salary in firm.items():
        file_obj.write(last_name + ':' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("file_1.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"persons: {persons}")
print(f"averate: {result}")

#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

translater = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
my_list = []
result = []
try:
    file_obj = open("file_2.txt", 'r')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word +' - '+ tokens[1])
    print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()

try:
    file_input = open("file_2.txt", "w")
    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_input.close()

#5. Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить
# ее на экран.

def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

#6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.

import json

subj = {}
with open('file_6.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')

#7. Создать (не программно) текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма
# собственности, выручка, издержки.
#Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
#Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')