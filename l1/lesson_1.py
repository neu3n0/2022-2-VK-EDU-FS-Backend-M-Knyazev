from curses.ascii import isalnum
import imp
from turtle import st


num = 42

print(
type(num),
isinstance(num, int), # является ли интом
id(num),
)

z = 14
y = 12
x = z or y  # Ленивые операции
print(x)

s = 'Test {}'.format(x)
print(s)

s = f'Test2 {x}'
print(s)

s = 'test'
s = s[1:4]
print(s)

s = 'test'
print(
s[::-1],
len(s),
s.capitalize(),
s.count('t'),
s.isalnum(),
)

s = '1'
print(s.isdigit())

s = 'test'

for x in s:
    print(x, end=' ')
else: # если выполнился весь for без break
    print()
    print('kek')

# if elif else


qwe = 4
x = qwe if qwe > 3 else None
print(x)


# Списки - упорядоченные изменяемые 

a = list()
a = []

qwe = [1, 2, 4]
print(qwe)

qwe = [1, 2, "ser"]
print(qwe)

qwe = [1, 2]
qwe = qwe * 2
print(qwe)

qwe = [1, 2, 4, 6, 9]

print(qwe[0])
print(qwe[1:3])
print(qwe[::-1])

print(qwe)

b = qwe
qwe.append(11)
print(b)

qwe = [1, 2, 4, 6, 8]
print(qwe)

qwe2 = qwe[:]
qwe.append(11)
print(qwe2)
qwe3 = qwe.copy()
qwe.append(12)
print(qwe3)

print()

qwe = [1, 2, 4, 6, 8]
print(qwe)

qwe = [4, 11, 2, 8, 1]

sorted(qwe) # не меняет qwe
print(qwe)

qwe.sort() # меняет qwe in place
print(qwe)

a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)

stud = [['Vanya', 21],['Anya', 23], ['Sanya', 20]]
print(stud)
print(sorted(stud))
print(sorted(stud, key=lambda x : x[1]))


a = ()
a = tuple()
a = 1,
# a = 1, # будет кортеж из 1, ))))))))))
print(a)
print(type(a))


dictT = dict()
dictT = {}
dictT = {"one":2, "two":4}
print(dictT)
print(dictT["one"])
print(dictT.get("three"))



print(11111111111111111111111111111111)
print()
for i in dictT.keys():
    print(i)

print()
for i in dictT:
    print(i)
print()
for i in dictT.values():
    print(i)
print()
for key,value in dictT.items():
    print(key, value)

print(11111111111111111111111)
print()

dictT.pop('two')
print(dictT)

del(dictT['one'])
print(dictT)

##### enumerate
qwe = {'Anya', 'Katya'}
for i, value in enumerate(qwe):
    print(i, value)

a = set()


a = [i ** 2 for i in range(10) if i % 2 == 0]
print(a)

b = {i: i ** 2 for i in range(10) if i % 2 == 0}
print(b)

def f(a: int) -> None:
    pass

# print(dir(f))

print(f.__annotations__)

def le(num):
    while num > 0:
        yield num 
        num -= 1

qwe = le(10)
print(*qwe)
# print(next(qwe))
# print(next(qwe))
# print(next(qwe))

print(type("Some", (object,), {"x": "hello"}))
