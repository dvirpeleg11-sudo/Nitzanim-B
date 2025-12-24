from shape import Shape

class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        print(f"Rectangle area is {self.width * self.height}.")