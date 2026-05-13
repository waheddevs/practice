''' K-TASK (PYTHON)

Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"

'''
# Masalaning yechimi:


def find_longest(text):

    words = text.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


print(find_longest('I am Arnold'))
print(find_longest('This is an Apple'))

''' I-TASK (PYTHON)

Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"

'''
# Masalaning yechimi:

'''
def get_digits(son):

    result = ""
    for char in son:
        if char.isdigit():
            result += char
    return result


print(get_digits("m14i1t"))
print(get_digits("a1b2c3"))
'''


''' G-TASK (PYTHON)

Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.

'''

'''
# Masalaning yechimi:
def get_highest_index(arr):
    max_value = max(arr)
    first_index = arr.index(max_value)

    return first_index


print(get_highest_index([3, 5, 10, 10, 2]))
print(get_highest_index([4, 9, 3]))
print(get_highest_index([6, 8, 25, 11]))

'''
