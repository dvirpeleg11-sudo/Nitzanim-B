from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def area(self):
        super().area()
        print(f"Square with side {self.side}.")