class Person:
    def __init__(self, name):
        self.__name = name  

    def get_name(self):
        return self.__name

p = Person("Алия")
print(p.get_name()) 
