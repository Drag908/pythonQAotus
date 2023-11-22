from datetime import datetime

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
import pytest


# @pytest.mark.skipif(reason="не работает в ноябре", condition=datetime.now().month == 10)
@pytest.mark.parametrize(("side_a", "side_b", "area", "perimetr"),
                         [(4, 6, 24, 20)])
def test_rectangle_positive(side_a, side_b, area, perimetr):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimetr"),
                         [(-4, -6, 24, -20)])
def test_rectangle_negative(side_a, side_b, area, perimetr):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} and {side_b}"
        assert r.get_area() == area
        assert r.get_perimetr() == perimetr


@pytest.mark.parametrize(("side_a", "area", "perimetr"),
                         [(4, 16, 16)])
def test_square(side_a, area, perimetr):
    r = Square(side_a)
    assert r.name == f"Square {side_a}"
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr


# def test_add_area():
#     r = Rectangle(2, 5)
#     s = Square(5)
#     assert r.add_area(s) == 35
#
#
# def test_add_area_negative():
#     r = Rectangle(2, 5)
#     c = Circle(10)
#     assert c.add_area(r) == 15
