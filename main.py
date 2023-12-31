from math import sqrt, pow


def cg_distance (x1, y1, x2, y2, x3, y3, x4, y4) -> float:
    """
    Функция находящая расстояние между центрами тяжести двух прямоугольников
    :param x1: Координата левого верхнего угла первого прямоуглольника
    :param y1: Координата левого верхнего угла первого прямоуглольника
    :param x2: Координата правого нижнего угла первого прямоугольника
    :param y2: Координата правого нижнего угла первого прямоугольника
    :param x3: Координата левого верхнего угла второго прямоуглольника
    :param y3: Координата левого верхнего угла второго прямоуглольника
    :param x4: Координата правого нижнего угла второго прямоугольника
    :param y4: Координата правого нижнего угла второго прямоугольника
    :return: расстояние между центрами тяжести двух прямоугольников
    """
    xc1 = (x1 + x2) / 2
    yc1 = (y1 + y2) / 2
    xc2 = (x3 + x4) / 2
    yc2 = (y3 + y4) / 2
    return sqrt(pow(xc1 - xc2, 2) + pow(yc1 - yc2, 2))

def corner_distance (x1, y1, x2, y2, x3, y3, x4, y4) -> float:
    """
    Функция находящая Сумму растояний между верхними левыми и
    нижними правыми углами
    :param x1: Координата левого верхнего угла первого прямоуглольника
    :param y1: Координата левого верхнего угла первого прямоуглольника
    :param x2: Координата правого нижнего угла первого прямоугольника
    :param y2: Координата правого нижнего угла первого прямоугольника
    :param x3: Координата левого верхнего угла второго прямоуглольника
    :param y3: Координата левого верхнего угла второго прямоуглольника
    :param x4: Координата правого нижнего угла второго прямоугольника
    :param y4: Координата правого нижнего угла второго прямоугольника
    :return: Сумма растояний между верхними левыми и нижними правыми углами
    """
    return (sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
            + sqrt(pow(x3-x4, 2) + pow(y3-y4, 2)))

if __name__ == "__main__":
    print(cg_distance( 1, 2, 3, 0,
                       3, 4, 5, 2,))
    print(corner_distance( 1, 2, 3, 0,
                           3, 4, 5, 2,))
