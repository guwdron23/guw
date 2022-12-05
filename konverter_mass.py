class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            print('Килограмм задаються только числами')
    @property
    def get_kg(self):
        return self.__kg




# g = KgToPounds(56)
# print(g.to_pounds())
a = KgToPounds
print(a.set_kg)


# def my_decor(func):
#     def wrapper():
#         print('start')
#         func()
#         print('end')
#     return wrapper
#
# @my_decor
# def my_func():
#     print('Тут основная функция')
#
# my_func()
