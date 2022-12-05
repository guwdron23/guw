class Soda:
    def __init__(self, dobavka):
        if isinstance(dobavka, str):
            self.dobavka = dobavka
        else:
            self.dobavka = None

    def show_my_drink(self):
        if self.dobavka:
            print(f'Газировка и {self.dobavka}')
        else:
            print('Обычная газировка')

s = Soda('Вода')
a = Soda('Кола')

print(s.dobavka)
print(a.dobavka)
print(s.show_my_drink())
print(a.show_my_drink())
