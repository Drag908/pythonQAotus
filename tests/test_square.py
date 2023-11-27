import pytest

from src.circle import Circle
from src.square import Square


@pytest.mark.parametrize(("side_a", "area", "perimetr"),
                         {
                             (4, 16, 16),
                             (3.5, 12.25, 14.0)
                         }, ids=["integer", "float"])
def test_square_positive(side_a, area, perimetr):
    r = Square(side_a)
    assert r.name == f"Square {side_a}"
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr


@pytest.mark.parametrize(("side_a", "area", "perimetr"),
                         {
                             (-4, -16, -16),
                             (0.0, 0.0, 18.1)
                         }, ids=["integer", "float"])
def test_square_negative(side_a, area, perimetr):
    with pytest.raises(ValueError):
        Square(side_a)


def test_add_area_square():
    s = Square(5)
    c = Circle(3)
    assert s.add_area(c) == 53.260000000000005
