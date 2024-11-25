from cmath import sqrt


def distance_between_points(a: tuple, b):
    return pow(pow(a.x - b.x, 2) + pow(a.y - b.y, 2), 0.5)


print(distance_between_points((10, 51), (18, 19)))
