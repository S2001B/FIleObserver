from math import pi

class Shape:
    def area(self) -> float:
        raise NotImplementedError()

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

def total_area(shapes: list[Shape]):
    return sum(shape.area() for shape in shapes)


shapes = [Square(4), Circle(3), Square(2)]
print(total_area(shapes))  # Should give the total combined area
