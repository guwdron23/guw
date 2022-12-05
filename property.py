class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property # Из метода делает атрибут
    def get_next_age(self):
        return self.age +1

p = Person('Marsel', 18)
print(p.get_next_age)


