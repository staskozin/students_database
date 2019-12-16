import unittest
from student import Student
from student_group import StudentGroup
from str_convert import (
    convert_student_to_str,
    convert_students_to_str,
    convert_students_to_file_str
)


class TestStrConvert(unittest.TestCase):
    def setUp(self):
        self.student = Student(10143634, 'Иванов И.И.', 2, 3.7, 19, 'м',
                               'Москва', 'Москва')
        self.group = StudentGroup()
        self.group.load_from_file('students.txt')

    def test_student(self):
        expected = (
            'Номер зачетки: 10143634\n'
            'ФИО: Иванов И.И.\n'
            'Год обучения: 2\n'
            'Средний балл: 3.7\n'
            'Возраст: 19\n'
            'Пол: м\n'
            'Место рождения: Москва\n'
            'Место проживания: Москва\n'
        )
        self.assertEqual(convert_student_to_str(self.student), expected)

    def test_students(self):
        expected = (
            'Номер зачетки  ФИО                       Год обучения  '
            'Средний балл  Возраст  Пол  Место рождения   Место проживания \n'
            '10143634       Иванов И.И.               2             '
            '4.3           18       м    Москва           Москва           \n'
            '10143635       Петров П.П.               2             '
            '4.1           19       м    Тула             Москва           \n'
            '10143636       Константинопольский К.К.  2             '
            '3.4           17       м    Пермь            Москва           \n'
            '10143637       Сидоров Н.В.              2             '
            '4.9           18       м    Санкт-Петербург  Москва           \n'
            '10143638       Иванова А.Г.              2             '
            '4.7           17       ж    Санкт-Петербург  Москва           \n'
        )
        self.assertEqual(convert_students_to_str(self.group.students),
                         expected)

    def test_students_to_file(self):
        expected = (
            '10143634;Иванов И.И.;2;4.3;18;м;Москва;Москва\n'
            '10143635;Петров П.П.;2;4.1;19;м;Тула;Москва\n'
            '10143636;Константинопольский К.К.;2;3.4;17;м;Пермь;Москва\n'
            '10143637;Сидоров Н.В.;2;4.9;18;м;Санкт-Петербург;Москва\n'
            '10143638;Иванова А.Г.;2;4.7;17;ж;Санкт-Петербург;Москва\n'
        )
        self.assertEqual(convert_students_to_file_str(self.group.students),
                         expected)


if __name__ == '__main__':
    unittest.main()
