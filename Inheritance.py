class Animal:
    def speak(self):
        print("Животное издаёт звук")

class Dog(Animal):
    def speak(self):
        print("Собака говорит: Гав-гав!")

dog = Dog()
dog.speak()  
