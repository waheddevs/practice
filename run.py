# Dunder - __builtins__, __init__         (Double Underscore)
message = 'PYTHON: Everything is an object'
print(message)

result = type(message)
print('Result:', result)


''' In Python, there are builtin tools:
(1) TYPES > int float str list dict
(2) FUNCTIONS > print() len() input() type()
(3) CONSTNTS > True False None
'''

# __builtins__ ro'yxatini olish:
print(dir (__builtins__))
