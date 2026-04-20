print('=== Iterable objects & RANGE ===')

# Iterable objects > takrorlanish xususiyatiga ega bo'lgan obyektlar
# Iterable objects > string dict tuple list range map filter

range_obj = range(3)  # 0, 3
print('range_obj:', range_obj)

for letter in 'MIT':
    print(f'letter: {letter}')
    for ele in range_obj:
        print(f'element: {ele}')


print('=== DICTIONARY ===')
# DICTIONARY is JSON object

person = {'name': 'Justin', 'age': 25, 'single': True}
person_obj = dict(name='Justin', age=25, single=True)
print(f'person: {person}')
print(f'person_obj: {person_obj}')

# method: get() > key orqali value ni olish
# name = person_obj['name']
name = person_obj.get('name')
hobby = person_obj.get('hobby')
balance = person_obj.get('balance', 0)
print(f'name: {name}, hobby: {hobby} and balance: {balance}')

del person_obj['single']
for key in person_obj:
    print(f'the key: {key} => value {person_obj.get(key)}')
