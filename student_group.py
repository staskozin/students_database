from student import Student


class StudentGroup():
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self):
        pass

    def update_student(self, student):
        pass

    def delete_student(self):
        pass

    def filter_students(self, test):
        return list(filter(test, self._students))

    def load_from_file(self, path):
        f = open(path, 'r')
        students = f.read().split('\n')
        del students[-1]
        f.close()
        self.students = [Student(*student.split(';')) for student in students]

    def save_to_file(self, path):
        f = open(path, 'w')
        for student in self.students:
            f.write(student.toFileRow())
        f.close()
