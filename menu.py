import os
from student import Student
from student_group import StudentGroup
from str_convert import (
    convert_student_to_str,
    convert_students_to_str
)
from num_convert import to_int, to_float


class Action:
    def __init__(self, name, action):
        self.name = name
        self.action = action


class Menu:
    def __init__(self):
        self.student_group = StudentGroup()
        self.actions = [
            Action(
                'Добавить студентов в список',
                self._add_students
            ),
            Action(
                'Вывести список студентов в виде таблицы',
                self._print_students
            ),
            Action(
                'Вывести студента по номеру зачетки',
                self._print_student
            ),
            Action(
                'Изменить студента по номеру зачетки',
                self._update_student
            ),
            Action(
                'Удалить студента по номеру зачетки',
                self._delete_student
            ),
            Action(
                'Получить список студентов из файла',
                self._load_students_from_file
            ),
            Action(
                'Сохранить список студентов в файл',
                self._save_students_to_file
            ),
        ]

    def execute_action(self, actionId):
        self.actions[actionId].action()

    def handle_input(self):
        os.system('cls')
        self._print_number_of_students()
        self._print_actions()
        chosen_action = to_int(input('Выберите действие: '))
        if chosen_action == 0:
            return
        elif chosen_action <= len(self.actions):
            os.system('cls')
            self.execute_action(chosen_action - 1)
        self.handle_input()

    def _print_number_of_students(self):
        if len(self.student_group.students) > 0:
            print(
                'Студентов в списке: ' +
                str(len(self.student_group.students))
            )
        else:
            print('Список студентов пуст')

    def _print_actions(self):
        print('\nДоступные действия:')
        for i, action in enumerate(self.actions):
            print(str(i + 1) + ' - ' + action.name)
        print('0 - Выход из программы')

    def _add_students(self):
        number_of_students = to_int(input('Сколько студентов добавить: '))
        for i in range(0, number_of_students):
            print('Студент ' + str(i + 1))
            record_book = to_int(input('Номер зачетки: '))
            while self.student_group.is_student_exists(record_book):
                print('Такой номер зачетки уже существует')
                record_book = to_int(input('Номер зачетки: '))
            name = input('ФИО: ')
            year_of_study = to_int(input('Год обучения: '))
            while year_of_study < 1 or year_of_study > 6:
                print('Год обучения может быть от 1 до 6')
                year_of_study = to_int(input('Год обучения: '))
            avg_grade = to_float(input('Средний балл: '))
            while avg_grade < 1 or avg_grade > 5:
                print('Средний балл может быть от 1 до 5')
                avg_grade = to_float(input('Средний балл: '))
            age = to_int(input('Возраст: '))
            gender = input('Пол: ')
            while gender not in Student.genders:
                print('Пол может быть только "м" или "ж"')
                gender = input('Пол: ')
            birth_place = input('Место рождения: ')
            living_place = input('Место проживания: ')

            self.student_group.add_student(
                Student(record_book, name, year_of_study, avg_grade,
                        age, gender, birth_place, living_place)
            )

    def _print_students(self):
        print(
            '1 - Вывести всех студентов\n'
            '2 - Отфильтровать студентов\n'
            '0 - Вернуться в главное меню\n'
        )
        chosen_action = to_int(input('Выберите действие: '))
        while chosen_action < 0 or chosen_action > 2:
            if chosen_action == 0:
                return
            print('Неверное действие')
            chosen_action = to_int(input('Выберите действие: '))

        if chosen_action == 1:
            os.system('cls')
            print(convert_students_to_str(self.student_group.students))
        elif chosen_action == 2:
            self._print_filtered_students()
        input('Для продолжения нажмите Enter...')

    def _print_filtered_students(self):
        os.system('cls')
        print(
            'По какому параметру фильтровать?\n'
            '1 - Год обучения\n'
            '2 - Средний балл\n'
            '3 - Возраст\n'
            '4 - Пол\n'
            '5 - Место рождения\n'
            '6 - Место проживания\n'
            '0 - Вернуться в главное меню\n'
        )
        chosen_action = to_int(input('Выберите параметр: '))
        while chosen_action < 0 or chosen_action > 6:
            if chosen_action == 0:
                return
            print('Неверный параметр')
            chosen_action = to_int(input('Выберите параметр: '))

        if chosen_action == 1:
            year_of_study = to_int(input('Год обучения: '))
            while year_of_study < 1 or year_of_study > 6:
                print('Год обучения может быть от 1 до 6')
                year_of_study = to_int(input('Год обучения: '))

            def equal(s): return s.year_of_study == year_of_study
            def less(s): return s.year_of_study < year_of_study
            def less_or_equal(s): return s.year_of_study <= year_of_study
            def more(s): return s.year_of_study > year_of_study
            def more_or_equal(s): return s.year_of_study >= year_of_study

            print(
                '1 - Равно\n'
                '2 - Меньше\n'
                '3 - Меньше или равно\n'
                '4 - Больше\n'
                '5 - Больше или равно\n'
            )
            chosen_action = to_int(input('Выберите действие: '))
            while chosen_action < 0 or chosen_action > 5:
                print('Неверное действие')
                chosen_action = to_int(input('Выберите действие: '))

            if chosen_action == 0 or chosen_action == 1:
                students = self.student_group.filter_students(equal)
            elif chosen_action == 2:
                students = self.student_group.filter_students(less)
            elif chosen_action == 3:
                students = self.student_group.filter_students(less_or_equal)
            elif chosen_action == 4:
                students = self.student_group.filter_students(more)
            elif chosen_action == 5:
                students = self.student_group.filter_students(more_or_equal)

            os.system('cls')
            print(convert_students_to_str(students))
        elif chosen_action == 2:
            avg_grade = to_float(input('Средний балл: '))
            while avg_grade < 1 or avg_grade > 5:
                print('Средний балл может быть от 1 до 5')
                avg_grade = to_float(input('Средний балл: '))

            def equal(s): return s.avg_grade == avg_grade
            def less(s): return s.avg_grade < avg_grade
            def less_or_equal(s): return s.avg_grade <= avg_grade
            def more(s): return s.avg_grade > avg_grade
            def more_or_equal(s): return s.avg_grade >= avg_grade

            print(
                '1 - Равно\n'
                '2 - Меньше\n'
                '3 - Меньше или равно\n'
                '4 - Больше\n'
                '5 - Больше или равно\n'
            )
            chosen_action = to_int(input('Выберите действие: '))
            while chosen_action < 0 or chosen_action > 5:
                print('Неверное действие')
                chosen_action = to_int(input('Выберите действие: '))

            if chosen_action == 0 or chosen_action == 1:
                students = self.student_group.filter_students(equal)
            elif chosen_action == 2:
                students = self.student_group.filter_students(less)
            elif chosen_action == 3:
                students = self.student_group.filter_students(less_or_equal)
            elif chosen_action == 4:
                students = self.student_group.filter_students(more)
            elif chosen_action == 5:
                students = self.student_group.filter_students(more_or_equal)

            os.system('cls')
            print(convert_students_to_str(students))
        elif chosen_action == 3:
            age = to_int(input('Возраст: '))

            def equal(s): return s.age == age
            def less(s): return s.age < age
            def less_or_equal(s): return s.age <= age
            def more(s): return s.age > age
            def more_or_equal(s): return s.age >= age

            print(
                '1 - Равно\n'
                '2 - Меньше\n'
                '3 - Меньше или равно\n'
                '4 - Больше\n'
                '5 - Больше или равно\n'
            )
            chosen_action = to_int(input('Выберите действие: '))
            while chosen_action < 0 or chosen_action > 5:
                print('Неверное действие')
                chosen_action = to_int(input('Выберите действие: '))

            if chosen_action == 0 or chosen_action == 1:
                students = self.student_group.filter_students(equal)
            elif chosen_action == 2:
                students = self.student_group.filter_students(less)
            elif chosen_action == 3:
                students = self.student_group.filter_students(less_or_equal)
            elif chosen_action == 4:
                students = self.student_group.filter_students(more)
            elif chosen_action == 5:
                students = self.student_group.filter_students(more_or_equal)

            os.system('cls')
            print(convert_students_to_str(students))
        elif chosen_action == 4:
            gender = input('Пол: ')
            while gender not in Student.genders:
                print('Пол может быть только "м" или "ж"')
                gender = input('Пол: ')
            students = self.student_group.filter_students(
                lambda s: s.gender == gender
            )
            os.system('cls')
            print(convert_students_to_str(students))
        elif chosen_action == 5:
            birth_place = input('Место рождения: ')
            students = self.student_group.filter_students(
                lambda s: s.birth_place == birth_place
            )
            os.system('cls')
            print(convert_students_to_str(students))
        elif chosen_action == 6:
            living_place = input('Место проживания: ')
            students = self.student_group.filter_students(
                lambda s: s.living_place == living_place
            )
            os.system('cls')
            print(convert_students_to_str(students))

    def _print_student(self):
        print('Вывод студента по номеру зачетки')
        record_book = int(input('Номер зачетки: '))
        if self.student_group.is_student_exists(record_book):
            os.system('cls')
            print(convert_student_to_str(
                self.student_group.get_student(record_book)
            ))
        else:
            print('Студента с таким номером зачетки не существует')
        input('Для продолжения нажмите Enter...')

    def _update_student(self):
        print('Изменение студента по номеру зачетки')
        record_book = int(input('Номер зачетки: '))
        if self.student_group.is_student_exists(record_book):
            os.system('cls')
            print(convert_student_to_str(
                self.student_group.get_student(record_book)
            ))

            student = self.student_group.get_student(record_book)

            print(
                'Что изменить?\n'
                '1 - Номер зачетки\n'
                '2 - ФИО\n'
                '3 - Год обучения\n'
                '4 - Средний балл\n'
                '5 - Возраст\n'
                '6 - Пол\n'
                '7 - Место рождения\n'
                '8 - Место проживания\n'
                '0 - Вернуться в главное меню\n'
            )
            chosen_action = to_int(input('Выберите действие: '))
            while chosen_action < 0 or chosen_action > 8:
                if chosen_action == 0:
                    return
                print('Неверное действие')
                chosen_action = to_int(input('Выберите действие: '))

            if chosen_action == 1:
                record_book = to_int(input('Номер зачетки: '))
                while self.student_group.is_student_exists(record_book):
                    print('Такой номер зачетки уже существует')
                    record_book = to_int(input('Номер зачетки: '))
                student.record_book = record_book
            elif chosen_action == 2:
                student.name = input('ФИО: ')
            elif chosen_action == 3:
                year_of_study = to_int(input('Год обучения: '))
                while year_of_study < 1 or year_of_study > 6:
                    print('Год обучения может быть от 1 до 6')
                    year_of_study = to_int(input('Год обучения: '))
                student.year_of_study = year_of_study
            elif chosen_action == 4:
                avg_grade = to_float(input('Средний балл: '))
                while avg_grade < 1 or avg_grade > 5:
                    print('Средний балл может быть от 1 до 5')
                    avg_grade = to_float(input('Средний балл: '))
                student.avg_grade = avg_grade
            elif chosen_action == 5:
                student.age = to_int(input('Возраст: '))
            elif chosen_action == 6:
                gender = input('Пол: ')
                while gender not in Student.genders:
                    print('Пол может быть только "м" или "ж"')
                    gender = input('Пол: ')
                student.gender = gender
            elif chosen_action == 7:
                student.birth_place = input('Место рождения: ')
            elif chosen_action == 8:
                student.living_place = input('Место проживания: ')

            self.student_group.update_student(record_book, student)
        else:
            print('Студент с таким номером зачетки не существует')
        input('Для продолжения нажмите Enter...')

    def _delete_student(self):
        print('Удаление студента по номеру зачетки')
        record_book = to_int(input('Номер зачетки: '))
        if self.student_group.is_student_exists(record_book):
            self.student_group.delete_student(record_book)
        else:
            print('Студента с таким номером зачетки не существует')
        input('Для продолжения нажмите Enter...')

    def _load_students_from_file(self):
        print('Получение списка студентов из файла')
        path = input('Введите путь к файлу: ')
        if os.path.isfile(path):
            self.student_group.load_from_file(path)
        else:
            print('Файла не существует')
            input('Для продолжения нажмите Enter...')

    def _save_students_to_file(self):
        print('Сохранение студента в файл')
        print('ВНИМАНИЕ! Предыдущее содержимое файла исчезнет')
        path = input('Введите путь к файлу: ')
        self.student_group.save_to_file(path)
        print('Студенты сохранены в файл ' + path)
        input('Для продолжения нажмите Enter...')
