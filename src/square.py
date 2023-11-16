from src.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Нельзя создать квадрат")
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.name = f"Square {side_a}"


s = Square(5)
print(s)
print(s.get_area())
