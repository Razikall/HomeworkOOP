import pytest

from HomeworkOOP.src.triangle import Triangle
from HomeworkOOP.src.square import Square
from HomeworkOOP.src.rectangle import Rectangle
from HomeworkOOP.src.circle import Circle


@pytest.fixture
def default_triangle():
    triangle = Triangle(11, 12, 13)
    yield triangle
    del triangle


@pytest.fixture
def wrong_triangle():
    false_triangle = Triangle(7, 7, 20)
    yield false_triangle
    del false_triangle


class WrongFigure:
    pass


@pytest.fixture
def wrong_figure():
    false_figure = WrongFigure
    yield false_figure
    del false_figure


@pytest.fixture
def default_square():
    square = Square(10)
    yield square
    del square


@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(14, 15)
    yield rectangle
    del rectangle


@pytest.fixture
def default_circle():
    circle = Circle(16)
    yield circle
    del circle
