#1) Создать 2 переменных типа String с разными значениями
a1 = ‘hello’
b1 = ‘world’
#2) Создать 4 переменных типа Integer с разными значениями
a, b, c, d = 1, 2, 3, 4
#3) Создать 3 переменных типа Float с разными значениями
a, b, c = 1.1, 2.3, 145.24 
# 4) Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
a, b, c = 22, 47, -17
print(a < b)
print(c < b)
print(a > c)
print(b > a)
print(b > c)
print(a >= c)
print(b >= a)
print(b >= c)
print(a <= b)
print( c <= a <= b)
print( c < a < b)
print( b > a > c)
print(a != b)
print(a != b != c)
print(a != c)

# 5) Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
a, b, c = 52.5, 32.7, -17.3
print(a > b)
print(c < b)
print(a > c)
print(b < a)
print(b > c)
print(a >= c)
print(b >= c)
print( a > b > c)
print( c < b < a)
print(a != b)
print(a != b != c)
print(a != c)

# 6) Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты весвести в консоль.
a, b, c = 22, 47, -17
print(a < b or c < b)
print(not a > b)
print(a >= c and b >= c)
print(c <= a <= b or c < a < b)
print(a != b or a != b != c)
print(not b <= a)


# 7) Сделать скрипт используя функцию input().
    1. Функция должна на вход принимать целое число.
    2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30" 
        a = int(input())

if a == 30:
    print('Вы ввели число', a, ', которое равно 30')
elif a > 30:
    print('Вы ввели число', a, ', которое больше 30')
else:
    print('Вы ввели число', a, ', которое меньше 30')

# 😍 Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу" 
    x = int(input())
import random
a = random.randint(1, 100)
if x > a:
    print('Вы ввели число', x, 'которое больше', a)
elif x == a:
    print('Вы ввели число', x, 'которое равно', a)
elif x < a:
    print('Вы ввели число', x, 'которое меньше', a)
else:
    print('Ошибка, обратитесь к разработчику')


# 9) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
x = int(input())
import random
a = random.randint(1, 100)
b = random.randint(1, 100)
print(a, b)
if a < x < b:
    print('Вы ввели число', x, 'которое больше', a, 'и меньше', b)
elif b < x < a:
    print('Вы ввели число', x, 'которое больше', b, 'и меньше', a)
elif b == x == a:
    print('Вы ввели число', x, 'которое равно', b, 'и равно', a)
elif a < x == b:
    print('Вы ввели число', x, 'которое больше', a, 'и равно', b)
elif a > x == a:
    print('Вы ввели число', x, 'которое равно', b, 'и меньше', a)
elif a == x > b:
    print('Вы ввели число', x, 'которое больше', b, 'и равно', a)
elif a == x < b:
    print('Вы ввели число', x, 'которое меньше', b, 'и равно', a)
elif x > a and x > b:
    print('Вы ввели число', x, 'которое больше', b, 'и больше', a)
elif x < a and x < b:
    print('Вы ввели число', x, 'которое меньше', b, 'и меньше', a)
else:
    print('Обратитесь к разработчику за исправлением бага')

# ----
# В заданиях 7, 8, 9, сами выберите какие условные операторы и сравнения использовать.
# 
# Ребята, чуток подредактировал 2-е задание в домашке по Python
# 9) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомных 2 целых числа (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"

