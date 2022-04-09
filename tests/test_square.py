import pytest


def test_name_square(default_square):
    assert default_square.name == "square"


def test_perimeter_square(default_square):
    assert default_square.perimeter == 40


def test_area_square(default_square):
    assert default_square.area == 100


def test_add_area_square(default_square, default_circle):
    assert default_square.add_area(default_circle) == 904


@pytest.mark.xfail
def test_add_area_wrong_figure(default_square, wrong_figure):
    assert default_square.add_area(wrong_figure) == 904
