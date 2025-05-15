class Cat:
    def sound(self):
        print("Кошка говорит: Мяу")

class Dog:
    def sound(self):
        print("Собака говорит: Гав")

def make_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()

make_sound(cat)  
make_sound(dog)
