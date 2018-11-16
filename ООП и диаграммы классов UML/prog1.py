
class Shape:
    def __init__(self, side, height):
        self.side = side
        self.height = height


class Triangle(Shape):
    def area(self):
        return self.side*self.height/2


class Rectangle(Shape):
    def area(self):
        return self.side*self.height


a = 10
b = 20
d = Triangle(a, b)
ans = d.area()
print(ans)
