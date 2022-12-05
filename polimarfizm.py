class Rectangle:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __str__(self) -> str:
        return f'Это прямоугольник {self.x} * {self.y} = {self.get_area()}'

class Square:
    def __init__(self, x: int):
        self.x = x

    def get_area(self):
        return self.x ** 2
    def __str__(self):
        return f'Это квадрат {self.x} ** 2 = {self.get_area()}'

class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        from math import pi
        return pi * self.r ** 2
    def __str__(self):
        return f'Это пи pi * {self.r} ** 2 = {self.get_area()}'

r = Rectangle(160, 60)
r1 = Rectangle(200, 140)
s = Square(3)
s1 = Square(5)
c = Circle(50)
c1 = Circle(25)

list_obj = [r, r1, s, s1, c, c1]

# for i in list_obj:
#     print(i)
#     if type(i) == Rectangle:
#         print(i.get_area_rectangle())
#     elif type(i) == Circle:
#         print(i.get_area_circle())
#     elif type(i) == Square:
#         print(i.get_area_square())


#Полимарфизм
for i in list_obj:
        print(i.get_area())
