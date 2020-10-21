#1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо
# использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.

from sys import argv

time, salary, bonus = argv

try:
    time = int(input('time'))
    salary = int(input('salary'))
    bonus = int(input('bonus'))
    res = time * salary + bonus
    print(f'заработная плата сотрудника {res}')
except ValueError:
    print('Not a number')

#2. Представлен список чисел. Необходимо вывести элементы исходного
# списка, значения которых больше предыдущего элемента.

my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

#4. Представлен список чисел. Определить элементы списка, не имеющие
# повторений. Сформировать итоговый массив чисел, соответствующих
# требованию. Элементы вывести в порядке их следования в исходном
# списке. Для выполнения задания обязательно использовать генератор.

my_list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)

#5. Реализовать формирование списка, используя функцию range() и
# возможности генератора. В список должны войти четные числа
# от 100 до 1000 (включая границы). Необходимо получить результат
# вычисления произведения всех элементов списка.

from functools import reduce

def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

#6. Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,

from itertools import count

stop = int(input('Введите шаг '))
for el in count(int(input('Введите стартовое число '))):
    if el > stop:
        break
    else:
        print(el)

#б) итератор, повторяющий элементы некоторого списка, определенного
# заранее.

from itertools import cycle

my_list= ["T", "A", "R", "B"]
iter = cycle(my_list)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

#7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим
# образом: for el in fact(n). Функция отвечает за получение
# факториала числа, а в цикле необходимо выводить только первые n
# чисел, начиная с 1! и до n!.

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
n = int(input("введите последнее число: "))
for i in gen:
    if x < n:
        print(i)
        x += 1
    else:
        break