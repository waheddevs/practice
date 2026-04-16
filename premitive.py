# Variable o'zi nima?
'''
Pythonda variable tushunchasi - REFERANCE ning nomlanishi deyiladi
'''
# in JAVA, variable is a name storage location
# in Python, variable is named referance

print('====== number ======')

count = 100
count_type = type(count)           # count type ini tekshirish uchun
# buning o'rniga quyidagi uslubdanfoydalaishimiz mumkin
print('count', count, count_type)
# bir qancha qiymatlarni bitta stringda namoyon qilishga yordam beradi
print(f'the count: {count} and type: {count_type}')

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)

print('====== string ======')
# METHODS(always used): upper() lower() title() find() replace()

course = 'AI Python Fullstack'
result = type(course)
print(f"the result (1): {result}")

result = course.title()  # method
print(f"the result (2): {result}")

result = course.upper()  # method
print(f"the result (3): {result}")

result = course.replace("Fullstack", "Masterclass")  # method
print(f"the result (4): {result}")
print(course)  # course o'zgarmadi, chunki yuqoridagi metodlar boshlang'ich qiymatga ta'sir qilmaydi. Qachonki biz result ni course ga tenglashtirsak, o'shanda course o'zgaradi
# course = course.replace("Fullstack", "Masterclass")

print('====== boolean ======')
