# Variable o'zi nima? 
'''
Pythonda variable tushuncha - REFERANCE ning nomlanishi deyiladi
'''
# in JAVA, variable is a name storage location
# in Python, variable is named referance

print('====== number ======')

count = 100
count_type = type(count)           # count type ini tekshirish uchun
print('count', count, count_type)  # buning o'rniga quyidagi uslubdanfoydalaishimiz mumkin
print(f'the count: {count} and type: {count_type}')     # bir qancha qiymatlarni bitta stringda namoyon qilishga yordam beradi

result1 = count.bit_count() # method
result2 = count.numerator # state 
print(result1, result2)