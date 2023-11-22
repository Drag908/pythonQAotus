from abc import ABC

from src.figure import Figure


class Circle(Figure, ABC):

    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Нельзя создать круг")
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def get_perimetr(self):
        return 2 * 3.14 * self.radius


s = Circle(10)
print(s.get_area())
print(s.get_perimetr())
