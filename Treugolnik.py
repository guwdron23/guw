class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура'
                return 'Жаль'
            return 'С отрицалами ничего не выйдет'
        return 'Только цифры'

a = TriangleChecker(200)
print(a.sides)
print(TriangleChecker.is_triangle())