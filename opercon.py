''' OPERATORS & CONDITIONS
(1) Operators
(2) Condition
(3) Logical operators

'''

print('==== Operators ====')
# + - > >= < <= == * is /         // % += **

a = 19
b = 5

'''
print('a > b', a > b)
print('a / b', a / b)
print('a * b', a * b)

'''

result = a // b   # Bo'linmaning butun qiymatni olib beradi
left = a % b      # qoldiqdagi natijani olib beradi
print(f'the result: {result} and left: {left}')

# a = a + 100
a += 100
print('a:', a)

print('b**2:', b**2)
print('b**3:', b**3)


print('='*5)

c = dict(name='Martin', age=35)
d = dict(name='Martin', age=35)
e = c

print('c==d', c == d)   # only compare value, not referance
print(id(c), id(d))

# data = c is d
print('c is d', c is d)
print('c is e', c is e)

# is - operatoridan biz referance ni ham value ni ham tekshirishda foydalanmaiz


print('==== Condition ====')
