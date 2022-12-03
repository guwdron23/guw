class Tomato:
    states = {
        1: 'Отсутствует',
        2: 'Цветение',
        3: 'Зеленый',
        4: 'Красный'
    }
    def __init__(self):
        self._index = 123
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:
    def __init__(self, amount):
        self.tomatoes = [Tomato(index) for index in range(0, amount)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, _plant):
        self.name = name
        self._plant = _plant

    def work(self):
        print('Gardener working')
        self._plant.grow_all()
        print('Gardener finished')

    def harvest(self):
        print('Gardener')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Gardener')
        else:
            print('Too early')

    @staticmethod
    def knowledge_base(self):
        print("""st""")


tomat = Tomato()
tomat.grow()
tomat.grow()
tomat.grow()



print(tomat._state)
print(tomat.is_ripe())