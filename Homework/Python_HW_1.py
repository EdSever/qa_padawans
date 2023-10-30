# 1) Создать переменную типа String

a = "Строка"
print('1) Создать переменную типа String')
print(type(a))
print()

# 2) Создать переменную типа Integer
b = 10
print('2) Создать переменную типа Integer')
print(type(b))
print()

# 3) Создать переменную типа Float
c = 5.5
print('3) Создать переменную типа Float')
print(type(c))
print()

# 4) Создать переменную типа Bytes
d = bytes(5)
print('4) Создать переменную типа Bytes')
print(type(d))
print()

# 5) Создать переменную типа List
f = ['Лист', 5, 6, 10.1]
print('5) Создать переменную типа List')
print(type(f))
print()

# 6) Создать переменную типа Tuple
e = (10, 20, 30)
print('6) Создать переменную типа Tuple')
print(type(e))
print()

# 7) Создать переменную типа Set
g = {1021222, 'Текст', (10, 20, 30)}
print('7) Создать переменную типа Set')
print(type(g))
print()

# 8) Создать переменную типа Frozen set
Number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
h = frozenset(Number)
print('8. Создать переменную типа Frozen set')
print(type(h))
print()

# 9) Создать переменную типа Dict
k = dict()
print('9) Создать переменную типа Dict')
k = {'name': 'Eduard', 'age': 38}
print(type(k))
print()

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print("10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных")
print("1.", a,type(a))
print("2.", b,type(b))
print("3.", c,type(c))
print("4.", d,type(d))
print("5.", f,type(f))
print("6.", e,type(e))
print("7.", g,type(g))
print("8.", h,type(h))
print("9.", k,type(k))
#print(" 1.", a, type(a), '\n', "2.", b, type(b), '\n',"3.", c, type(c), '\n', "4.", d, type(d), '\n', "5.", f, type(f),
      # '\n', "6.", e, type(e), '\n', "7.", g, type(g), '\n', "8." , h, type(h), '\n', "9.", k, type(k))
print()

# 11) Создать 2 переменные String, создать переменную в которой канкатенируете эти переменные. Вывести в консоль.
print('11) Создать 2 переменные String, создать переменную в которой канкатенируете эти переменные. Вывести в консоль.')
s1 = 'Конкатенация'
s2 = " строк"
s3 = ' в Python.'
s = s1 + s2 + s3
print(s)
print()

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print('12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)')
s4 = 'February'
i1 = 28
print(s4, i1, sep=',')
print()

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print('13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)')
s4 = 'February'
i1 = 28
print(s4, i1, sep='+')
print()
