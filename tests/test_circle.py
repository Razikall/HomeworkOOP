import pytest


def test_name_circle(default_circle):
    assert default_circle.name == "circle"


def test_perimeter_circle(default_circle):
    assert default_circle.perimeter == 100


def test_area_circle(default_circle):
    assert default_circle.area == 804


def test_add_area_circle(default_circle, default_rectangle):
    assert default_circle.add_area(default_rectangle) == 1014


@pytest.mark.xfail
def test_add_area_wrong_circle(default_circle, wrong_figure):
    assert default_circle.add_area(wrong_figure) == 1014
