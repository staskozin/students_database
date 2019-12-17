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
                self._addStudensToList
            ),
            Action(
                'Вывести список студентов в виде таблицы',
                self._printAllStudentsAsTable
            ),
            Action(
                'Вывести студента по номеру зачетки',
                self._printStudentById
            ),
            Action(
                'Изменить студента по номеру зачетки',
                self._updateStudentById
            ),
            Action(
                'Удалить студента по номеру зачетки',
                self._deleteStudentById
            ),
            Action(
                'Получить список студентов из файла',
                self._getStudentsFromFile
            ),
            Action(
                'Сохранить список студентов в файл',
                self._saveStudentsToFile
            ),
            Action(
                'Вывести кол-во девушек в списке',
                self._printNumberOfGirls
            ),
        ]

    def executeAction(self, actionId):
        self.actions[actionId].action()

    def handleInput(self):
        os.system('cls')

        self._printNumberOfStudents()

        print('\nДоступные действия:')
        for i, action in enumerate(self.actions):
            print(str(i + 1) + ' - ' + action.name)
        print('0 - Выход из программы')

        chosenAction = int(input('Выберите действие: '))
        if chosenAction == 0:
            return
        elif chosenAction <= len(self.actions):
            os.system('cls')
            self.executeAction(chosenAction - 1)
        self.handleInput()

    def _printNumberOfStudents(self):
        if len(self.student_group.students) > 0:
            print(
                'Студентов в списке: ' +
                str(len(self.student_group.students))
            )
        else:
            print('Список студентов пуст')

    def _addStudensToList(self):
        number_of_students = int(input('Сколько студентов добавить: '))
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
            age = input('Возраст: ')
            gender = input('Пол: ')
            while gender not in Student.genders:
                print('Пол может быть только "м" или "ж"')
                gender = input('Пол: ')
            birthPlace = input('Место рождения: ')
            livingPlace = input('Место проживания: ')

            self.student_group.add_student(
                Student(record_book, name, year_of_study, avg_grade,
                        age, gender, birthPlace, livingPlace)
            )

    def _printAllStudentsAsTable(self):
        print(convert_students_to_str(self.student_group.students))
        input('Для продолжения нажмите Enter...')

    def _printStudentById(self):
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

    def _updateStudentById(self):
        print('Изменение студента по номеру зачетки')
        record_book = int(input('Номер зачетки: '))
        if self.student_group.is_student_exists(record_book):
            os.system('cls')
            print(convert_student_to_str(
                self.student_group.get_student(record_book)
            ))

            print('Новые данные: ')
            name = input('ФИО: ')
            year_of_study = to_int(input('Год обучения: '))
            while year_of_study < 1 or year_of_study > 6:
                print('Год обучения может быть от 1 до 6')
                year_of_study = to_int(input('Год обучения: '))
            avg_grade = to_float(input('Средний балл: '))
            while avg_grade < 1 or avg_grade > 5:
                print('Средний балл может быть от 1 до 5')
                avg_grade = to_float(input('Средний балл: '))
            age = input('Возраст: ')
            gender = input('Пол: ')
            while gender != 'м' and gender != 'ж':
                print('Пол может быть только "м" или "ж"')
                gender = input('Пол: ')
            birthPlace = input('Место рождения: ')
            livingPlace = input('Место проживания: ')

            self.student_group.update_student(
                record_book,
                Student(record_book, name, year_of_study, avg_grade,
                        age, gender, birthPlace, livingPlace)
            )
        else:
            print('Студента с таким номером зачетки не существует')
        input('Для продолжения нажмите Enter...')

    def _deleteStudentById(self):
        print('Удаление студента по номеру зачетки')
        record_book = int(input('Номер зачетки: '))
        if self.student_group.is_student_exists(record_book):
            self.student_group.delete_student(record_book)
        else:
            print('Студента с таким номером зачетки не существует')
        input('Для продолжения нажмите Enter...')

    def _getStudentsFromFile(self):
        print('Получение списка студентов из файла')
        path = input('Введите путь к файлу: ')
        if os.path.isfile(path):
            self.student_group.load_from_file(path)
        else:
            print('Файла не существует')
            input('Для продолжения нажмите Enter...')

    def _saveStudentsToFile(self):
        print('Сохранение студента в файл')
        print('ВНИМАНИЕ! Предыдущее содержимое файла исчезнет')
        path = input('Введите путь к файлу: ')
        self.student_group.save_to_file(path)
        print('Студенты сохранены в файл ' + path)
        input('Для продолжения нажмите Enter...')

    def _printNumberOfGirls(self):
        numberOfGirls = len(
            self.student_group.filter_students(lambda x: x.gender == 'ж')
        )
        print('Кол-во девушек в списке: ' + str(numberOfGirls))
        input('Для продолжения нажмите Enter...')
