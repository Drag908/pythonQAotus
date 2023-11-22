import pytest

from src.rectangle import Rectangle
from src.triangle import Triangle


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimetr"),
                         {
                             (5, 5, 5, 10.825317547305483, 15),
                             (3.3, 5.5, 6.6, 9.05481087599294, 15.4)
                         }, ids=["integer", "float"])
def test_triangle_positive(side_a, side_b, side_c, area, perimetr):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimetr"),
                         {
                             (-5, -5, -5, 10.825317547305483, 15),
                             (0.0, 0.0, 6.6, 9.05481087599294, 15.4)
                         }, ids=["integer", "float"])
def test_triangle_negative(side_a, side_b, side_c, area, perimetr):
    with pytest.raises(ValueError):
        r = Triangle(side_a, side_b, side_c)
        assert r.name == f"Rectangle {side_a} and {side_b} and {side_c}"
        assert r.get_area() == area
        assert r.get_perimetr() == perimetr


def test_add_area_triangle():
    t = Triangle(5, 5, 5)
    r = Rectangle(3, 8)
    assert t.add_area(r) == 34.82531754730548
