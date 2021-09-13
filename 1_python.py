#Создать переменную типа String
a= 'go'
b= 'to school'
print(a, b)
print('type =', type(a))

# Создать переменную типа Integer
num1 = 123
a1 = num1//100
a2 = (num1//10)%10
a3 = num1%10
print(num1, '- это', a1, 'сотня,', a2,'десятка,', a3, 'единицы.')
print('type =', type(a3))

# Создать переменную типа Float
num3 = 2.3
num4 = 5.2
print(num3, '*', num4, '=', num3*num4, sep='')
print('type =', type(num3*num4))

# Создать переменную типа Bytes
line = "choke python"
res = bytes(line, 'utf-8')
print(res)
print('type =', type(res))

num5 = 5
num6 = bytes(num5)
print(num6)
print('type =', type(num6))

# Создать переменную типа List
k = 'adventure'
print(list(k))
print('type =', type(k))

# Создать переменную типа Tuple
a = tuple('hello!')
print(a)

tuple1 = ('aa', 'bb', 'cc')
print(tuple1[0])
print('type =', type(tuple1))

# Создать переменную типа Set
settype1= {'1', '2', '3', '4', '1', '2', '3', '4'}
print(settype1)
print('type =', type(settype1))
print(set(range(11)))


# Создать переменную типа Frozen set
list1 =  [1, 2, 3, 4, 5]
frozet = frozenset(list1)
print(frozet)
print('type =', type(frozet))

# Создать переменную типа Dict
nums = {'Belarus' : 'Minsk', 'UK' : 'London', 'Bali' : 'Denpasar'}
print(nums)
print(nums['UK'])
print('type =', type(nums))

# Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
param1 = 'go'
param2 = 'home'
param3 = ' '
print(param1+param2)
print(param1+param3+param2)

# Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
param4 = 110
param5 = 15
param6 = param4+param5
aa1 = param6//100
aa2 = (param6//10)%10
aa3 = param6%10
print('(', param4, '+', param5, '=', param6, ')', ' /', aa1, ' - это сотни, ', aa2,' - это десятки, ', aa3, ' - это единицы.', sep='')

# Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
param7 = param4/param5
param8 = param4//param5
param9 = param7-param8
print(param7, '- это', param8, 'целых и', param9*100, 'сотых')

# Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
param10 = param4*param5
print('x=', param4, 'y=', param5, 'x*y=', param10, 'x^y=', param4**param5)

# Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
print('При делении', param4, 'на', param5, 'без остатка, получается', param8, 'целых')

# Создать переменную в которой надо присвоить остаток от деления этих переменные Int.
param11 = param4%param5
print('Остаток от деления', param4, 'на', param5, 'составляет', param11)
