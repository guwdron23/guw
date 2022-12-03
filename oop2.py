class Mebel:
    def __init__(self, title: str, area: int):
        self.title = title
        self.area = area

    def __str__(self):
        return f'{self.title} {self.area}'

class Home:
    def __init__(self, title: str, area: int, mebels: list):
        self.title = title
        self.area = area
        self.mebels = mebels

    def get_area(self):
        count = 0
        for mebel in self.mebels:
            count += mebel.area
        return self.area - count

    def get_mebels(self):
        mebel_names = []
        for mebel in self.mebels:
            mebel_names.append(mebel.title)
        return mebel_names

    def __str__(self):
        return f'{self.title} {self.area}'

class Person:
    def __init__(self, name: str, age: int, homes: list):
        self.name = name
        self.age = age
        self.homes = homes

    def get_homes_name(self) -> list:
        home_name = []
        for home in self.homes:
            home_name.append(home.title)
        return home_name

    def get_homes_area(self) -> int:
        count = 0
        for home in self.homes:
            count += home.area
        return count

    def get_mebels_name(self) -> list:
        mebel_names = []
        for home in self.homes:
            for mebel in home.mebels:
                mebel_names.append(mebel.title)
        return mebel_names

    def get_mebels_area(self) -> int:
        count = 0
        for home in self.homes:
            for mebel in home.mebels:
                count += mebel.area
        return count






shkaf = Mebel('Shkaf', 4)
shkaf1 = Mebel('Shkaf из Индии', 4)
table = Mebel('Table', 5)
bad = Mebel('Bad', 3)

#home1 = Home('Дом Султана', 125, [shkaf, shkaf1, table, bad, bad])
#print(home1.get_area())
#print(home1.get_mebels())

#home1.mebels.append(shkaf1)

#print(home1.get_mebels())

home1 = Home('Дом Султана', 125, [shkaf, shkaf1, table, bad, bad])
home2 = Home('Дом Али', 250, [shkaf, shkaf1, table, bad, bad])
home3 = Home('Дом Ислама', 80, [shkaf, shkaf1, table, bad, bad])
print(Person)