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
print(animals[0])
animals[0] = 'bird'
