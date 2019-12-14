import os
from students import Student, StudentGroup


class Action:
    def __init__(self, name, action):
        self.name = name
        self.action = action


class Menu:
    def __init__(self):
        self.studentGroup = StudentGroup()
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
        if len(self.studentGroup.students) > 0:
            print(
                'Студентов в списке: ' +
                str(len(self.studentGroup.students))
            )
        else:
            print('Список студентов пуст')

    def _addStudensToList(self):
        numberOfStudents = int(input('Сколько студентов добавить: '))
        for i in range(0, numberOfStudents):
            print('Студент ' + str(i + 1))
            studentId = int(input('Номер зачетки: '))
            while self.studentGroup.isIdExists(studentId):
                print('Такой номер зачетки уже существует')
                studentId = int(input('Номер зачетки: '))
            name = input('ФИО: ')
            age = input('Возраст: ')
            gender = input('Пол: ')
            while gender != 'м' and gender != 'ж':
                print('Пол может быть только "м" или "ж"')
                gender = input('Пол: ')
            birthPlace = input('Место рождения: ')
            livingPlace = input('Место проживания: ')

            self.studentGroup.addStudent(
                Student(studentId, name, age, gender, birthPlace, livingPlace)
            )

    def _printAllStudentsAsTable(self):
        self.studentGroup.printAsTable()
        input('Для продолжения нажмите Enter...')

    def _printStudentById(self):
        print('Вывод студента по номеру зачетки')
        studentId = int(input('Номер зачетки: '))
        if self.studentGroup.isIdExists(studentId):
            os.system('cls')
            self.studentGroup.printStudentById(studentId)
        else:
            print('Студента с таким номером зачетки не существует')
        input('Для продолжения нажмите Enter...')

    def _updateStudentById(self):
        print('Изменение студента по номеру зачетки')
        studentId = int(input('Номер зачетки: '))
        if self.studentGroup.isIdExists(studentId):
            os.system('cls')
            self.studentGroup.printStudentById(studentId)

            print('\nНовые данные: ')
            name = input('ФИО: ')
            age = input('Возраст: ')
            gender = input('Пол: ')
            while gender != 'м' and gender != 'ж':
                print('Пол может быть только "м" или "ж"')
                gender = input('Пол: ')
            birthPlace = input('Место рождения: ')
            livingPlace = input('Место проживания: ')

            self.studentGroup.updateStudentById(
                studentId,
                Student(studentId, name, age, gender, birthPlace, livingPlace)
            )
        else:
            print('Студента с таким номером зачетки не существует')
        input('Для продолжения нажмите Enter...')

    def _deleteStudentById(self):
        print('Удаление студента по номеру зачетки')
        studentId = int(input('Номер зачетки: '))
        if self.studentGroup.isIdExists(studentId):
            self.studentGroup.deleteStudentById(studentId)
        else:
            print('Студента с таким номером зачетки не существует')
        input('Для продолжения нажмите Enter...')

    def _getStudentsFromFile(self):
        print('Получение списка студентов из файла')
        path = input('Введите путь к файлу: ')
        if os.path.isfile(path):
            self.studentGroup.getStudentsFromFile(path)
        else:
            print('Файла не существует')
            input('Для продолжения нажмите Enter...')

    def _saveStudentsToFile(self):
        print('Сохранение студента в файл')
        print('ВНИМАНИЕ! Предыдущее содержимое файла исчезнет')
        path = input('Введите путь к файлу: ')
        self.studentGroup.saveStudentsToFile(path)
        print('Студенты сохранены в файл ' + path)
        input('Для продолжения нажмите Enter...')

    def _printNumberOfGirls(self):
        numberOfGirls = len(list(filter(
            lambda x: x.gender == 'ж',
            self.studentGroup.students
        )))
        print('Кол-во девушек в списке: ' + str(numberOfGirls))
        input('Для продолжения нажмите Enter...')
