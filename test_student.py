import unittest
from student import Student, to_int, to_float


class TestRecordBook(unittest.TestCase):
    def setUp(self):
        self.student = Student(10143634, 'Иванов И.И.', 2, 3.7, 19, 'м',
                               'Москва', 'Москва')

    def test_normal(self):
        self.assertEqual(self.student.record_book, 10143634)

    def test_negative(self):
        self.student.set_record_book(-10143634)
        self.assertEqual(self.student.record_book, 10143634)

    def test_string(self):
        self.student.set_record_book('10143634')
        self.assertEqual(self.student.record_book, 10143634)

    def test_wrong_string(self):
        self.student.set_record_book('wrong')
        self.assertEqual(self.student.record_book, 0)


class TestYearOfStudy(unittest.TestCase):
    def setUp(self):
        self.student = Student(10143634, 'Иванов И.И.', 2, 3.7, 19, 'м',
                               'Москва', 'Москва')

    def test_normal(self):
        self.assertEqual(self.student.year_of_study, 2)

    def test_negative(self):
        self.student.set_year_of_study(-1)
        self.assertEqual(self.student.year_of_study, 1)

    def test_string(self):
        self.student.set_year_of_study('1')
        self.assertEqual(self.student.year_of_study, 1)

    def test_wrong_string(self):
        self.student.set_year_of_study('wrong')
        self.assertEqual(self.student.year_of_study, 1)

    def test_big_number(self):
        self.student.set_year_of_study(10)
        self.assertEqual(self.student.year_of_study, 6)

    def test_zero(self):
        self.student.set_year_of_study(0)
        self.assertEqual(self.student.year_of_study, 1)


class TestAvgGrade(unittest.TestCase):
    def setUp(self):
        self.student = Student(10143634, 'Иванов И.И.', 2, 3.7, 19, 'м',
                               'Москва', 'Москва')

    def test_normal(self):
        self.assertEqual(self.student.avg_grade, 3.7)

    def test_negative(self):
        self.student.set_avg_grade(-3.7)
        self.assertEqual(self.student.avg_grade, 3.7)

    def test_string(self):
        self.student.set_avg_grade('3.9')
        self.assertEqual(self.student.avg_grade, 3.9)

    def test_wrong_string(self):
        self.student.set_avg_grade('wrong')
        self.assertEqual(self.student.avg_grade, 1.0)

    def test_big_number(self):
        self.student.set_avg_grade(10)
        self.assertEqual(self.student.avg_grade, 5.0)

    def test_zero(self):
        self.student.set_avg_grade(0)
        self.assertEqual(self.student.avg_grade, 1.0)


class TestAge(unittest.TestCase):
    def setUp(self):
        self.student = Student(10143634, 'Иванов И.И.', 2, 3.7, 19, 'м',
                               'Москва', 'Москва')

    def test_normal(self):
        self.assertEqual(self.student.age, 19)

    def test_negative(self):
        self.student.set_age(-19)
        self.assertEqual(self.student.age, 19)

    def test_string(self):
        self.student.set_age('19')
        self.assertEqual(self.student.age, 19)

    def test_wrong_string(self):
        self.student.set_age('wrong')
        self.assertEqual(self.student.age, 0)


class TestGender(unittest.TestCase):
    def setUp(self):
        self.student = Student(10143634, 'Иванов И.И.', 2, 3.7, 19, 'м',
                               'Москва', 'Москва')

    def test_normal(self):
        self.assertEqual(self.student.gender, 'м')

    def test_wrong(self):
        self.student.set_gender(1)
        self.assertEqual(self.student.gender, '-')


class TestDefaultValues(unittest.TestCase):
    def test_to_int(self):
        self.assertEqual(to_int('a'), 0)

    def test_to_float(self):
        self.assertEqual(to_float('a'), 0)


class TestPrint(unittest.TestCase):
    def setUp(self):
        self.student = Student(10143634, 'Иванов И.И.', 2, 3.7, 19, 'м',
                               'Москва', 'Москва')

    def test_single(self):
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
        self.assertEqual(str(self.student), expected)

    def test_table(self):
        pass

    def test_file(self):
        pass


if __name__ == '__main__':
    unittest.main()
