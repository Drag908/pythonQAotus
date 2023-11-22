import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimetr"),
                         {
                             (4, 6, 24, 20),
                             (3.5, 5.5, 19.25, 18.0)
                         }, ids=["integer", "float"])
def test_rectangle_positive(side_a, side_b, area, perimetr):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimetr"),
                         {
                             (-4, -6, -24, -20),
                             (0.0, 5.5, 19.26, 18.1)
                         }, ids=["integer", "float"])
def test_rectangle_negative(side_a, side_b, area, perimetr):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} and {side_b}"
        assert r.get_area() == area
        assert r.get_perimetr() == perimetr


def test_add_area_rectangle():
    r = Rectangle(2, 5)
    s = Square(5)
    assert r.add_area(s) == 35
