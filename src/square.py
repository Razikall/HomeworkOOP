# Атрибуты и расчеты для квадрата
from HomeworkOOP.src.figure import Figure


class Square(Figure):

    # Конструктор квадрата
    def __init__(self, side_a):
        self.name = 'square'
        self.side_a = side_a

    # Название фигуры
    def get_name(self):
        return self.name

    # Расчет периметра квадрата
    @property
    def perimeter(self):
        return self.side_a * 4

    # Расчет площади квадрата
    @property
    def area(self):
        return self.side_a * self.side_a
