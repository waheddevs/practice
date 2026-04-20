''' OBJECTS - malum bir maqsadda yaratilgan o'zining state hamda methodlariga ega bo'lgan maxsus datatype.

(1) What is object?
(2) Iterable objects & RANGE
(3) DICTIONARY
(4) Error handling system

'''

import array  # packkage/module
import math  # packkage
from math import ceil
print('=== What is object? ===')
# An object has state and method properties
# Everything is an object in Python

print(type('Hello World'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigma(uslubiyat) > Functional programming & OOP
# OOP 4 CONCETS > Abstraction / Encapsulation / Inheritance / Polymorphism
result1 = math.ceil(97.7)  # CALL
print('result1:', result1)

result2 = ceil(98.7)  # CALL
print('result2:', result2)
