from .person import Person

class Student(Person):
    def __init__(self, first_name, last_name, subject_area):
        super(Student, self).__init__(first_name, last_name)
        self.subject_area = subject_area
    def printNameSubject(self):
        print(f"{self.first_name} {self.last_name}, {self.subject_area}")
