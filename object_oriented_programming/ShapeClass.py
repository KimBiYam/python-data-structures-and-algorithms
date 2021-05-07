import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"point ({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"({self.x!r}, {self.y!r})"


class Circle(Point):
    def __init__(self, radius, x, y):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.raidus and super().__eq__(other)

    def __repr__(self):
        return f"circle ({self.radius!r}, {self.x!r})"

    def __str__(self):
        return repr(self)


if __name__ == "__main__":
    point = Point(3, 4)
    print(point)
    print(repr(point))
    print(str(point))
    print(point.distance_from_origin())

    circle = Circle(3, 2, 1)
    print(circle)
    print(repr(circle))
    print(str(circle))
    print(circle.circumference())
    print(circle.edge_distance_from_origin())
