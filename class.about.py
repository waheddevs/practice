''' CLASS
(1) What is class?
(2) ordinary vs static propierties
(3) special methods

'''

print('=== What is class? ===')
# class - blueprint for creating objects
# class - state constructor method


class Person():
    # state
    message = 'class state property'
    # constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass
    # method

    def introduce(self):
        print(f'{self.name} says: How do you do!')

    def say_age(self):
        print(f'{self.name} says: I am {self.age}!')

    @classmethod
    def explain(cls):
        print('static method property executed')


person1 = Person('ARNOLD', 25)  # object creation
person2 = Person('John', 20)  # object creation
person3 = Person('LEO', 22)  # object creation

# ordinary state property
print('person1 name:', person1.name)

# ordinary method
person1.introduce()
person2.say_age()


print('=== ordinary vs static propierties ===')
# static state
new_message = Person.message
print('new_message:', new_message)

# static object doim class lar bilan bog'liq bo'ladi, ya'ni class ni o'zgartirsak, static object ham o'zgaradi

# static method
Person.explain()


print('=== special(magic) methods ===')
# python's most common special meyhods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...


class Car():
    # state
    description = 'This class makes car'
    # constructor

    def __new__(cls, *args):
        print('*__new__*')
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year
    # method

    def start_engine(self):
        print(f'the{self.name} started engine!')

    def stop_engine(self):
        print(f'the{self.name} stopped engine!')

    def __str__(self):
        return f'Car name: {self.name} was produced in {self.year}'

    def __call__(self):
        print('Object called as a function!')
        return True


my_car = Car('Ferrari', 2025)
my_car.start_engine()
my_car.stop_engine()

print('-------')
your_car = Car('Tayota', 2026)
print(your_car)
response = your_car()
print('response:', response)
