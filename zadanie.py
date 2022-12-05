#
# class Factory:
#     def engine(self):
#         return ('Дигатель создан')
#
#     def bridge(self):
#         return ('Ходовая часть создана')
#
# class Toyota(Factory):
#     def wheels(self):
#         return ('Колёса готовы')
#     def windows(self):
#         return ('Стёкла готовы')
#
# t = Toyota()
# toyota1 = []
# toyota1.append(t.engine())
# toyota1.append(t.bridge())
# toyota1.append(t.wheels())
# toyota1.append(t.windows())
# print(toyota1)
#
# class Zoo:
#     animal_1 = 'Тигр'
#     animal_2 = 'Бегемот'
#     animal_3 = 'Жираф'
#     animal_4 = [animal_2, animal_3]
#
# z = Zoo.animal_4
# print(z)


class Car:
    def __init__(self, motor, wheels, windows):
        self.motor = motor
        self.wheels = wheels
        self.windows = windows

    def ride(self):
        print('Ездить')

    def door(self):
        print('Открывать дверь')

class Jeep(Car):
    def __init__(self, motor, wheels, windows, awd):
        super().__init__(motor, wheels, windows)
        self.awd = awd

class Pickup(Jeep):
    def __init__(self, motor, wheels, windows, awd, trailer, ):
        super().__init__(motor, wheels, windows, awd)
        self.trailer = trailer

    def ride_mountain(self):
        print('Ездить по горам')

class Cargo(Car):
    def __init__(self, motor, wheels, windows, trailer):
        super().__init__(motor, wheels, windows)
        self.trailer = trailer

    def carry_cargo(self):
        print('Возить груз')

class Kamaz(Cargo):
    def haul_lift(self):
        print('Возить поднять')

car1 = Kamaz(Kamaz.haul_lift())

#
# class House():
#     """Описание дома"""
#     def __init__(self, street, number):
#         """свойства дома"""
#         self.street = street
#         self.number = number
#         self.age = 2000
#
#     def build(self):
#         """Стройт дом"""
#         print(f'Дом на улице {self.street} под номером {self.number} построен {abs(house1.age)} года назад')
#
#     def age_of_house(self, year):
#         """Возраст дома"""
#         self.age -= year
#
# house1 = House('Сейфуллина', 15)
# House2 = House('Сейфуллина', 20)
# house1.age_of_house(2022)
# print(house1.age)
# print(house1.build())
#
# class Prospekt(House):
#     """дома на проспекте"""
#
#     def __init__(self, prospekt, number):
#         super().__init__(self, number)
#         self.prospekt = prospekt
#
# PrHouse = Prospekt('Абай', 5)
# print(PrHouse.prospekt, PrHouse.number)
