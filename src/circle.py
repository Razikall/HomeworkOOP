# Атрибуты и расчеты для круга
import math
from HomeworkOOP.src.figure import Figure


class Circle(Figure):

    # Конструктор круга
    def __init__(self, side_a):
        self.name = 'circle'
        self.side_a = side_a

    # Название фигуры
    def get_name(self):
        return self.name

    # Расчет периметра круга
    @property
    def perimeter(self):
        return int(2 * self.side_a * math.pi)

    # Расчет площади круга
    @property
    def area(self):
        return int(math.pi * self.side_a ** 2)

    # Расчет суммы площадей, если пришла фигура, соответствующая классу Figure
    def add_area(self, some_figure):
        if isinstance(some_figure, Figure):
            return self.area + some_figure.area
        else:
            raise ValueError("Incorrect class")
