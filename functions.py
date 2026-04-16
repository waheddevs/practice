''' FUNCTIONS
(1) DEFINE vs CALL
(2) PARAMETER vs ARGUMENT
(3) KEYWORD vs DEFUALT ARGUMENT
(4) SCOPE
'''

print('====== DEFINE vs CALL ======')
# build in function > print() type()
# Function - reusable block of code (malum bir mantiqni ishga tushuruvchi kod blok)
# Instead of block {} in JAVA, we use indentation in Python to define a function (:)
# def - function definition

# DEFINE - build


def great(a):            # void function, chunki return yo'q
    print(f"How do you do, {a}")


def greating(b):         # return function, chunki return bor
    return f"Hi, {b}"


# CALL -execute
great('ARNOLD')

'''
result1 = great('ARNOLD')
print("the result1:", result1)
# None, chunki function ichida return yo'q, shuning uchun default qiymat None bo'ladi

'''

result2 = greating('MARTIN')
print("the result2:", result2)
