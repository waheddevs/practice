''' Tuple
(1) What is tuple: tuple vs list
(2) Unpacking arguments
(3) zip

'''

print('===== What is tuple: tuple vs list =====')
# Java/PHP/NodeJS array => Python list (array = list)

# literal
numbs = [3, 5, 1, 2]
# car_dic = {'brand': 'Ferrari', 'year': 1995}
# print(numbs)

# constructor
letters = list('Hello World!')
# person_dict = dict(name='Martin', age=35)
# print(letters)

# index dagi valueni o'zgartirish
fruits = ['apple', 'lemon', 'banana', 'kiwi']
print('before fruits:', fruits)

fruits[2] = 'melon'
print('after fruits:', fruits)

# Biz hosil qilgan malumotlarni himoyalashda bizga TUPLE yordam beradi
animals = ('dog', 'cat', 'fish', 'lion')
tuple_obj = ('MIT', 1000, True, None)

# we can not change Tuple - ()
# print(animals[0])
# animals[0] = 'bird'

# try avoid this (bu holatda qavslarsiz tuple hosil qilish xato emas, lekin bu uslub source imizni tushunarsiz holatga olib kelishi mumkin)
# people = 'Andrew', 'John'

print('===== Unpacking arguments =====')

groups = ['MIT', 'FLEXY', 'DEVEX', 'MG']
# Pythonda Bu guruhlarni argumentlarga yoyishda Tuple lar orqali amalga oshiriladi
(x, y, z, a) = groups
(x, y, *z) = groups  # (bu uslubda x hamda y birinchi va ikkinchi grouplarg yoyilsa, *z - undan keyingi kelgan barcha guruhlar z ga yoyilsin degan manoni anglatadi)
print(f'the x: {x} and y: {y}')
print('z:', z)  # list


# * - args(argument > tuple)
def calculate(*args):
    print('*args >', *args)
    total = 1
    for x in args:
        total *= x
    print(f'the type(args) value: {type(args)}')
    print(f'the total value: {total}')
    return total


# call
calculate(1, 7, 2, 3)
print('-------')
calculate(0, 2, 300)
print('-------')
calculate(5, 7)

# Qachonki argumentlarimiz soni noaniq bo'lsa, Tuple ga wrap qilib argumentlarni yoyishda ishlatamiz


# **kwargs > dictionary lar orqali hosil bo'lgan uslubiyat
def introduce(*args, **keywargs):
    pass


# call
introduce(name='Justin', age=28)
introduce(name='Shawn', age=30, single=True)
