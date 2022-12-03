from time import sleep
from random import choice

class Gun:
    def __init__(self, name: str, number_bullets: int):
        self.name = name
        self.number_bullets = number_bullets
        self.bullets = 0

    def change_mag(self):
        self.bullets = self.number_bullets
        print('Перезаряжаюсь, Прикрой')
        sleep(2)

    def shot(self):
        if self.bullets ==0:
            print('Нет патронов')
        if self.bullets > 0:
            for i in range(1, self.bullets+1):
                print(f'{choice("😁😝🥵 ")}Shot -->')
                sleep(0.2)
                if self.bullets == 2:
                    print('Последний патрон')
                if i % 3 ==0:
                    print()
                    sleep(0.5)
                self.bullets -= 1

#ak47 = Gun('Ak-47', 20)
#ak47.change_mag()
#ak47.shot()

class Soldier:
    def __init__(self, name: str, weapon: Gun, mag: int):
        self.name = name
        self.weapon = weapon
        self.mag = mag

    def atak(self):
        while self.mag != 0:
            self.weapon.change_mag()
            self.mag -= 1
            print('Готов к Бою')
            if self.mag == 0:
                print('Последний магазин')
            self.weapon.shot()

            if self.mag == 0:
                print('Конец мага, нам пздц')

ak47 = Gun('Ak47', 20)
soldier = Soldier('Islam', ak47, 3)
soldier.atak()