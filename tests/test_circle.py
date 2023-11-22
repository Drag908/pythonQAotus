import pytest

from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize(("radius", "area", "perimetr"),
                         {
                             (3, 28.26, 18.84),
                             (2.5, 19.625, 15.700000000000001)
                         }, ids=["integer", "float"])
def test_circle_positive(radius, area, perimetr):
    r = Circle(radius)
    assert r.name == f"Square {radius}"
    assert r.get_area() == area
    assert r.get_perimetr() == perimetr


@pytest.mark.parametrize(("radius", "area", "perimetr"),
                         {
                             (-3, -16, -16),
                             (0.0, 0.0, 18.1)
                         }, ids=["integer", "float"])
def test_circle_negative(radius, area, perimetr):
    with pytest.raises(ValueError):
        r = Circle(radius)
        assert r.name == f"Rectangle {radius}"
        assert r.get_area() == area
        assert r.get_perimetr() == perimetr


def test_add_area_circle():
    c = Circle(3)
    t = Triangle(5, 5, 5)
    assert c.add_area(t) == 39.085317547305486
