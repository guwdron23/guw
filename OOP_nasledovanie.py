class Person:
    def __init__(self, name, age, specialization):
        self.name = name
        self.age = age
        self.specialization = specialization

    def __str__(self):
        return f'[{self.specialization} по имени {self.name}'

    def eat(self):
        print(f'{self.name} {self.specialization} кушает')

    def sleep(self):
        print(f'{self.name} {self.specialization} спит')

    def love(self):
        print(f'{self.name} {self.specialization} любит')


class Doctor(Person):
    def heal(self):
        print(f'{self.name} {self.specialization} лечит')

class Fireman(Person):
    def tushit(self):
        print(f'{self.specialization} {self.name} тушить огонь')

class Teacher(Person):
    def teach(self):
        print(f'{self.specialization} {self.name} Учить')

    def heal(self):
        print(f'лечу как хочуzada}')

teacher1 = Teacher('Kiri', 16, 'Python Backend development')
print(teacher1)