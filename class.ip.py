''' CLASS deep dive
(1) ENCAPSULATION
(2) INHERITANCE
(3) POLYMORPHISM

'''

print('==== INHERITANCE ====')

# Meros bo'lib o'tish manosini anglatadi. 2 ta class bo'ladi,parent hamda child. bu bo'limda parent class child class ga bazi propertylarni pass qiladi
# Parent o'zining public hamda protected propertylarini(state, method) child classga taqdim qila oladi. Private ni O'TKAZOLMAYDI


class Animal:     # Parent
    # state
    descripotion = 'the class is parent for Animals'

    # constructor
    def __init__(self, voice):
        self._status = 'animal is alive'
        self.voice = voice

    # method
    def make_voice(self):
        print(f'The animal can make voice: {self.voice}')


class Dog(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        # super() orqali child valeu ni yani voice ni parent class ga yuboradi
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f'{self.name} says: {self.sound}-{self.sound}')

    def protect(self):
        print('Yes, I can protect you!')


class Cat(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        # super() orqali child valeu ni yani voice ni parent class ga yuboradi
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f'{self.name} says: {self.sound}-{self.sound}')

    def play(self):
        pass


class Fish(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        # super() orqali child valeu ni yani voice ni parent class ga yuboradi
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f'{self.name} says: {self.sound}-{self.sound}')

    def swim(self):
        print('Yes, I can swim!')


dog = Dog('Rex', 'wow', True)
cat = Cat('Tom', 'myeow', True)
fish = Fish('Nemo', 'Zzz', False)

dog.introduce()
cat.introduce()
fish.introduce()

print('--------')
dog.make_voice()
fish.make_voice()

print('---------')
print((Animal).descripotion)
print(Dog.descripotion)

print(dog.voice, fish.voice)
print('status:', dog._status)
