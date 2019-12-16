import unittest
import os
from student import Student
from student_group import StudentGroup
from str_convert import convert_students_to_str


class TestStudentGroup(unittest.TestCase):
    def setUp(self):
        self.student = Student(10143639, 'Иванов И.И.', 2, 3.7, 19, 'м',
                               'Москва', 'Москва')
        self.group = StudentGroup()
        self.group.load_from_file('students.txt')

    def test_is_student_exists(self):
        self.assertTrue(self.group.is_student_exists(10143634))
        self.assertFalse(self.group.is_student_exists(10143639))

    def test_add_student(self):
        expected = self.group.students + [self.student]
        self.group.add_student(self.student)
        self.assertListEqual(self.group.students, expected)

        # Проверяем, что уже существующий студент не добавится
        self.group.add_student(self.student)
        self.assertListEqual(self.group.students, expected)

    def test_add_student_wrong(self):
        expected = self.group.students.copy()
        self.group.add_student('wrong')
        self.assertListEqual(self.group.students, expected)

    def test_update_student(self):
        self.group.update_student(10143634, self.student)
        self.assertFalse(self.group.is_student_exists(10143634))

    def test_delete_students(self):
        expected = self.group.students.copy()
        self.group.students += [self.student]
        self.group.delete_student(10143639)
        self.assertListEqual(self.group.students, expected)

    def test_filter_students(self):
        self.assertEqual(
            len(self.group.filter_students(lambda s: s.avg_grade > 4.2)), 3
        )

    def test_save_to_file(self):
        f = open('students.txt', 'r')
        expected = f.read()
        f.close()
        self.group.save_to_file('students_test.txt')
        f = open('students_test.txt', 'r')
        test = f.read()
        f.close()
        self.assertEqual(test, expected)
        os.remove('students_test.txt')

    def test_load_from_file(self):
        group = StudentGroup()
        group.load_from_file('students.txt')
        self.assertEqual(convert_students_to_str(group.students),
                         convert_students_to_str(self.group.students))


if __name__ == '__main__':
    unittest.main()
