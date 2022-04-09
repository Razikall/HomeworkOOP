class Figure:

    def __init__(self):
        self.area = 0

    # Расчет суммы площадей, если пришла фигура, соответствующая классу Figure
    def add_area(self, some_figure):
        if isinstance(some_figure, Figure):
            return self.area + some_figure.area
        else:
            raise ValueError("Incorrect class")
