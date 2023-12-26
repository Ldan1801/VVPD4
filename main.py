from math import sqrt, pow


def cg_distance (x1, y1, x2, y2, x3, y3, x4, y4) -> float:
    X1 = (x1+x2)/ 2
    Y1 = (y1+y2)/ 2
    X2 = (x3 + x4) / 2
    Y2 = (y3 + y4) / 2
    return sqrt(pow(X1-X2, 2) + pow(Y1-Y2, 2))

def corner_distance (x1, y1, x2, y2, x3, y3, x4, y4) -> float:
    return (sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
            + sqrt(pow(x3-x4, 2) + pow(y3-y4, 2)))

print(cg_distance( 1, 2, 3, 0, 3, 4, 5, 2,))
print(corner_distance( 1, 2, 3, 0, 3, 4, 5, 2,))