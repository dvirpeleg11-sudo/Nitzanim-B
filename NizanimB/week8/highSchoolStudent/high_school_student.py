from student import Student

class HighSchoolStudent(Student):

    def __init__(self, name, school, grade):
        super().__init__(name, school)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"I am in grade {self.grade}")