import Person

class Student(Person):

    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def introduce(self):
        super().introduce()
        print(f"I study at {self.school}.")