''' List
(1) Working with lists
(2) List methods
(3) Lambda function
(4) enumerate, map and filter

'''

print('====== Working with lists ======')
# Java/PHP/NodeJS array => Python - list

# literal
person = {'name': 'Justin', 'age': 25}     # dictionary
people = ('Andrew', "John", 'Micheal')     # tuple
groups = ['MIT', 'FLEXY', 'DEVEX', 'MG']   # list
for team in groups:
    print(f'the team: {team}')

# constructor
result = list('Hello World')
print(f'the result: {result} and the size: {len(result)}')

print('-------')
fruits = ['apple', 'orange', 'lemon' 'kiwi']
a = fruits[0]
print("-----")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals", animals)

animals.remove("lion")
print("remove: ", animals)

del animals[2:4]
print("animals delete: ", animals)

exists = animals.index("cat")
print("cat exists: ", exists)

animals.clear()
print("animals clear:", animals)

numbers = [2, 20, 12, 8, 5]
numbers.sort()
print("sort default: ", numbers)

numbers.sort(reverse=True)
print("sort revers: ", numbers)

# sorted
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"sorted numbs: {numbs} and new numbs: {new_numbs}")

# lamda function
# labmda is small anonymous function
print("=== lambda function ===")


def calculate(x, y):
    return x * y


result = calculate(3, 5)
print("result: ", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael ", 30),
    ("Ali", 23),
]
people.sort()
print(people)

# sort  by age via lambda
people.sort(key=lambda person: person[1])
print("people2: ", people)

print("=== enumerate, map, filter ===")
# enumerate for index & value
animals = ["dog", "cat", "fish"]
for element in enumerate(animals):
    print("element: ", element)
print("-----")

for (index, value) in enumerate(animals):
    print(f"index: {index}, value: {value}")

# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2025)
result = car_obj.items()
for (key, value) in result:
    print(f"key: {key}, value: {value}")

print("------")
# map
cars = [
    ("ferrari", 128),
    ("Toyota", 103),
    ("Audi", 28),
    ("BmW", 48),
    ("Mers", 12),
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new car(1): ", new_cars)

result_map = map(lambda car: car[0], cars)
new_cars = list(result_map)
print("new cars(2): ", new_cars)


print("------")
# filter

result_filter = filter(lambda car: car[1] > 80, cars)
print(list(result_filter))
b = fruits[0:2]   # Bunda 2 gacha bo'lgan valuelni oliberadi, lekin 2 ni emas
# Birinchi va 3 qadam sakrab keyingi elementni olishni buyrug'i hisoblanadi
c = fruits[::3]
d = fruits[::-1]  # Qiymatlarni oxiridan boshlab olib beradi

print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)


print('====== List methods ======')
# methods > append() insert() pop() remove() clear() sort() index()

letters = ['a', 'd', 'b']

letters.append('c')   # add behind
print(f'the append result: {letters}')

# append() insert() pop() remove() clear() sort() - mutable methods

letters.insert(0, 'z')  # add front
print(f'the insert result: {letters}')

size = len(letters) - 1
result = letters.pop(size)   # pop behind (valeu ni olib tashlashda ishlatmiz)
print(f'the pop result: {result} and the letters: {letters}')

result2 = letters.pop(0)   # pop front
print(f'the pop result: {result2} and the letters: {letters}')

print("-----")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals", animals)

animals.remove("lion")
print("remove: ", animals)

del animals[2:4]
print("animals delete: ", animals)

exists = animals.index("cat")
print("cat exists: ", exists)

animals.clear()
print("animals clear:", animals)

numbers = [2, 20, 12, 8, 5]
numbers.sort()
print("sort default: ", numbers)

numbers.sort(reverse=True)
print("sort revers: ", numbers)

# sorted
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"sorted numbs: {numbs} and new numbs: {new_numbs}")

# lamda function
# labmda is small anonymous function
print("=== lambda function ===")


def calculate(x, y):
    return x * y


result = calculate(3, 5)
print("result: ", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael ", 30),
    ("Ali", 23),
]
people.sort()
print(people)

# sort  by age via lambda
people.sort(key=lambda person: person[1])
print("people2: ", people)

print("=== enumerate, map, filter ===")
# enumerate for index & value
animals = ["dog", "cat", "fish"]
for element in enumerate(animals):
    print("element: ", element)
print("-----")

for (index, value) in enumerate(animals):
    print(f"index: {index}, value: {value}")

# similar in dictionaries
car_obj = dict(brand="Ferrari", year=2025)
result = car_obj.items()
for (key, value) in result:
    print(f"key: {key}, value: {value}")

print("------")
# map
cars = [
    ("ferrari", 128),
    ("Toyota", 103),
    ("Audi", 28),
    ("BmW", 48),
    ("Mers", 12),
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
print("new car(1): ", new_cars)

result_map = map(lambda car: car[0], cars)
new_cars = list(result_map)
print("new cars(2): ", new_cars)


print("------")
# filter

result_filter = filter(lambda car: car[1] > 80, cars)
print(list(result_filter))
