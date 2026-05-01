''' G-TASK (PYTHON)

Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.

'''

# Masalaning yechimi:


def get_highest_index(arr):
    max_value = max(arr)
    first_index = arr.index(max_value)

    return first_index


print(get_highest_index([3, 5, 10, 10, 2]))
print(get_highest_index([4, 9, 3]))
print(get_highest_index([6, 8, 25, 11]))
