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
# Condition lar true hamda false ni emas, balki TRUTHY & FALTHY qiymatlarni tekshiradi

# TRUTHY: True 100 -100 'MIT'
# FALTHY: false 0 "" None

x = 15

if x > 50:
    print('Case A')
elif x > 10:             # elif = else if
    print('Case B')
else:
    print('Case c')

print('-------')


print('==== Logical operators ====')

age = 21
'''
person = None
if age > 16:
    person = 'adult'
else:
    person = 'child'

'''

# TERNARY = logical operators
person = 'adult' if age > 18 else 'minor'
print('person:', person)

print('-------')

is_student = True
is_admin = False
is_guest = True
is_parent = True

'''
if is_student:
    print('Executed')

'''
if not is_student:
    print('Welcome here, do you want to be a student')
elif is_admin:
    print('please go to the office')
elif is_guest or is_parent:          # or operatorida qatnashgan qiymatlardan hech bo'lmaganda bittasi True bo'lsa natija True bo'ladi
    print('waiting room is over there')
# elif is_guest and is_parent:          # and operatorida qatnashgan qiymatlardan hech bo'lmaganda bittasi False bo'lsa natija False bo'ladi
#   print('waiting room is over there')
else:
    print('Etc')
