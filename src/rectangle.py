# Атрибуты и расчеты для прямоугольника
from HomeworkOOP.src.figure import Figure


class Rectangle(Figure):

    # Конструктор прямоугольника
    def __init__(self, side_a, side_b):
        self.name = 'rectangle'
        self.side_a = side_a
        self.side_b = side_b

    # Название фигуры
    def get_name(self):
        return self.name

    # Расчет периметра прямоугольника
    @property
    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    # Расчет площади прямоугольника
    @property
    def area(self):
        return self.side_a * self.side_b

    # Расчет суммы площадей, если пришла фигура, соответствующая классу Figure
    def add_area(self, some_figure):
        if isinstance(some_figure, Figure):
            return self.area + some_figure.area
        else:
            raise ValueError("Incorrect class")
