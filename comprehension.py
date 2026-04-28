''' Comprehension
(1) What is Comprehension & list comp
(2) set and dictionary comp

'''

print('===== What is Comprehension & list comp =====')
# Comprehension acts like spread operator (... - three little dots. We can use to handle all arrays with one operator)

''' Comprehension general syntax
a) *iterable
b) <expression> for item in iterable
C) <expression> for item in iterable <conditions>
'''

# list comprehension
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]        # a version
# list_numbers = numbers         # True
print('list_numbers:', list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

# Xulosa: Comprehention metodi numbers listni faqat raqamlaridan foydalangan holda butunlay yangi referance ga egabo'lgan listlarni hosil qilishda yordam berar ekan

print('-------')
people = [('Robert', 20), ('Steve', 19), ('Joseph', 25)]
list_people = [person[0] for person in people]      # b version

print('list_people', list_people)


cars = [
    ('Ferrari', 78),
    ('Tayota', 98),
    ('Audi', 116),
    ('BMW', 109),
    ('Pagani', 33)
]
list_cars = [car[0] for car in cars if car[1] > 80]    # c version
print('list_cars', list_cars)


print('===== set and dictionary comp =====')
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}              # a version
print('set_numbs:', set_numbs)
# Bu amalimiz arraydagi bir xil value larni bitta qilib olishda ishlatiladi. Agar 2 ta bir value bo'lsa ulardan faqat bittasini oladi

dict_people = {person[0]: person[1] for person in people}    # b version
print('dict_people', dict_people)

dict_people2 = {person[0]: person[1]
                for person in people if person[1] > 20}      # c version
print('dict_people2', dict_people2)


# (expression> for item in iterable) generic
# generic typelardan katta hajmdagi malumotlar bilan ishlaganda foydalanimiz. Generic type lar ko'p ishlatilmaganligi uchun bunga chuqur to'xtalmaymiz
