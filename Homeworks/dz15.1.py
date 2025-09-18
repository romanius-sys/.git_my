import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Можна додавати тільки прямокутники")
        new_area = self.get_square() + other.get_square()
        # робимо новий прямокутник зі сторонами 1 і new_area
        return Rectangle(1, new_area)

    def __mul__(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Множити можна тільки на додатне число")
        new_area = self.get_square() * n
        # робимо новий прямокутник зі сторонами 1 і new_area
        return Rectangle(1, new_area)

    __rmul__ = __mul__  # щоб працювало і 4 * r1

    def __str__(self):
        return f"Rectangle({self.width} x {self.height}), area = {self.get_square()}"


# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("Усі тести пройдені")