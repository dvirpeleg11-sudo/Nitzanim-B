class Shape:

    def __init__(self, shape_name):
        self.shape_name = shape_name

    def area(self):
        print(f"{self.shape_name} cannot calculate area because the required dimensions are missing.")