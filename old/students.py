class Student:
    def __init__(self, studentId, name, age, gender, birthPlace, livingPlace):
        self.studentId = int(studentId)
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.birthPlace = birthPlace
        self.livingPlace = livingPlace

    def __str__(self):
        return (
            'Номер зачетки: ' + str(self.studentId) + '\n' +
            'ФИО: ' + self.name + '\n' +
            'Возраст: ' + str(self.age) + '\n' +
            'Пол: ' + self.gender + '\n' +
            'Место рождения: ' + self.birthPlace + '\n' +
            'Место проживания: ' + self.livingPlace + '\n'
        )

    def toTableRow(self):
        return (
            '{:<15}'.format(self.studentId) +
            '{:<26}'.format(self.name) +
            '{:<9}'.format(self.age) +
            '{:<5}'.format(self.gender) +
            '{:<17}'.format(self.birthPlace) +
            '{:<17}'.format(self.livingPlace)
        )

    def toFileRow(self):
        return (
            str(self.studentId) + ';' +
            self.name + ';' +
            str(self.age) + ';' +
            self.gender + ';' +
            self.birthPlace + ';' +
            self.livingPlace + '\n'
        )


class StudentGroup:
    def __init__(self):
        self.students = []

    def isIdExists(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                return True

    def addStudent(self, student):
        self.students.append(student)

    def updateStudentById(self, studentId, newStudent):
        for i, student in enumerate(self.students):
            if student.studentId == studentId:
                self.students[i] = newStudent
                break

    def deleteStudentById(self, studentId):
        for i, student in enumerate(self.students):
            if student.studentId == studentId:
                del self.students[i]
                break

    def printStudentById(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                print(student)

    def printAsTable(self):
        print(
            '{:<15}'.format('Номер зачетки') +
            '{:<26}'.format('ФИО') +
            '{:<9}'.format('Возраст') +
            '{:<5}'.format('Пол') +
            '{:<17}'.format('Место рождения') +
            '{:<17}'.format('Место проживания')
        )
        for student in self.students:
            print(student.toTableRow())

    def saveStudentsToFile(self, path):
        f = open(path, 'w')
        for student in self.students:
            f.write(student.toFileRow())
        f.close()

    def getStudentsFromFile(self, path):
        f = open(path, 'r')
        students = f.read().split('\n')
        del students[-1]
        f.close()
        self.students = [Student(*student.split(';')) for student in students]
