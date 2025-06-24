import random

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


hitbox = Rectangle(100, 200)

print(hitbox.area())
print(hitbox.perimeter())

rectangles = [
    Rectangle(random.randint(50, 100), random.randint(50, 100))
    for _ in range(100)
]

for rect in rectangles:
    print(rect.width, rect.height)

print(
    sum([
        rect.area()
        for rect in rectangles
    ]) / len(rectangles)
)
