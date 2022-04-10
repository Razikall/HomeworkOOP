import pytest


def test_name_rectangle(default_rectangle):
    assert default_rectangle.name == "rectangle"


def test_perimeter_rectangle(default_rectangle):
    assert default_rectangle.perimeter == 58


def test_area_rectangle(default_rectangle):
    assert default_rectangle.area == 210


def test_add_area_rectangle(default_rectangle, default_triangle):
    assert default_rectangle.add_area(default_triangle) == 271


@pytest.mark.xfail
def test_add_area_wrong_rectangle(default_rectangle, wrong_figure):
    assert default_rectangle.add_area(wrong_figure) == 161
