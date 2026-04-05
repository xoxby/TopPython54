import math


def calculate_area(figure_type, **kwargs):
    if figure_type == 'rhombus':
        d1 = kwargs.get('d1', 0)
        d2 = kwargs.get('d2', 0)
        return (d1 * d2) / 2

    elif figure_type == 'square':
        a = kwargs.get('a', 0)
        return a ** 2

    elif figure_type == 'trapezoid':
        a = kwargs.get('a', 0)
        b = kwargs.get('b', 0)
        h = kwargs.get('h', 0)
        return 0.5 * (a + b) * h

    elif figure_type == 'circle':
        r = kwargs.get('r', 0)
        return math.pi * r ** 2

    else:
        return "invalid data"


print(calculate_area('rhombus', d1=10, d2=8))
print(calculate_area('square', a=5))
print(calculate_area('trapezoid', a=12, b=3, h=6))
print(calculate_area('circle', r=18))
print(calculate_area('unknown', a=1, b=2, c=3))
