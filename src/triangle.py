# Атрибуты и расчеты для треугольника
import math
from HomeworkOOP.src.figure import Figure


class Triangle(Figure):

    # Конструктор треугольника с проверкой, что создаваемая фигура является треугольником
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b:
            self.name = 'triangle'
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            raise ValueError("Figure != Triangle")

    # Название фигуры
    def get_name(self):
        return self.name

    # Расчет периметра треугольника
    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    # Расчет площади треугольника
    @property
    def area(self):
        h_per = (self.side_a + self.side_b + self.side_c) / 2
        return int(math.sqrt(h_per * (h_per - self.side_a) * (h_per - self.side_b) * (h_per - self.side_c)))
