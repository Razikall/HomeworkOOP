import pytest


def test_name_triangle(default_triangle):
    assert default_triangle.name == "triangle"


def test_perimeter_triangle(default_triangle):
    assert default_triangle.perimeter == 36


def test_area_triangle(default_triangle):
    assert default_triangle.area == 61


@pytest.mark.xfail
def test_figure_is_not_triangle(wrong_triangle):
    assert wrong_triangle.perimeter == 36


def test_add_area_triangle(default_triangle, default_square):
    assert default_triangle.add_area(default_square) == 161


@pytest.mark.xfail
def test_add_area_wrong_figure(default_triangle, wrong_figure):
    assert default_triangle.add_area(wrong_figure) == 161
