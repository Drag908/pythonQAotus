from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a + side_b <= side_c or side_b + side_c <= side_a or side_a + side_c <= side_b:
            raise ValueError("Нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a} and {side_b} and {side_c}"

    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c


r = Triangle(5, 5, 5)
print(r.get_area())
print(r.get_perimetr())
