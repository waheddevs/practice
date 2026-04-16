''' FUNCTIONS
(1) DEFINE vs CALL
(2) PARAMETER vs ARGUMENT
(3) KEYWORD vs DEFAULT ARGUMENT
(4) SCOPE
'''


print('====== DEFINE(parameter) vs CALL(argument) ======')
# build in function > print() type()
# Function - reusable block of code (malum bir mantiqni ishga tushuruvchi kod blok)
# Instead of block {} in JAVA, we use indentation in Python to define a function (:)
# def - function definition


# DEFINE - build (parameter)


def great(a):            # void function, chunki return yo'q
    print(f"How do you do, {a}")


def greating(b):         # return function, chunki return bor
    return f"Hi, {b}"


# CALL -execute function (argument)
great('ARNOLD')

'''
result1 = great('ARNOLD')
print("the result1:", result1)
# None, chunki function ichida return yo'q, shuning uchun default qiymat None bo'ladi

'''

result2 = greating('MARTIN')
print("the result2:", result2)


print('====== KEYWORD vs DEFAULT ARGUMENT ======')

# DEFINE


# default argument, agar age ni argument sifatida bermasak, default qiymat 25 bo'ladi
def give_great(name, age=25):
    print('give_great is executed')
    return f'Hi, {name}, you are {age} years old!'


# CALL
result3 = give_great('ARNOLD', 76)
# result3 = give_great(name='ARNOLD', age=76)   # KEYWORD ARGUMENT / biz bundan mantig'imizni yanada aniqroqifodalash uchun ishlatamiz
print("the result3:", result3)

# age argumentini bermadik, shuning uchun default qiymat 25 bo'ladi
result4 = give_great('MARTIN')
print("the result4:", result4)


print('====== KEYWORD vs DEFAULT ARGUMENT ======')
