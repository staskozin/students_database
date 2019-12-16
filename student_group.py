from student import Student
from str_convert import convert_students_to_file_str


class StudentGroup():
    def __init__(self):
        self.students = []

    def is_student_exists(self, record_book):
        for student in self.students:
            if student.record_book == record_book:
                return True

    def add_student(self, student):
        if isinstance(student, Student):
            if not self.is_student_exists(student.record_book):
                self.students.append(student)

    def update_student(self, record_book, new_student):
        for i, student in enumerate(self.students):
            if student.record_book == record_book:
                self.students[i] = new_student
                break

    def delete_student(self, record_book):
        for i, student in enumerate(self.students):
            if student.record_book == record_book:
                del self.students[i]
                break

    def filter_students(self, test):
        return list(filter(test, self.students))

    def load_from_file(self, path):
        f = open(path, 'r')
        students = f.read().split('\n')
        del students[-1]
        f.close()
        self.students = [Student(*student.split(';')) for student in students]

    def save_to_file(self, path):
        f = open(path, 'w')
        f.write(convert_students_to_file_str(self.students))
        f.close()
