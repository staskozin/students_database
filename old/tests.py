from students import Student, StudentGroup


stud = Student(1, 'петуч', 18, 'м', 'Москва', 'Москва')
print(stud)

studs = StudentGroup([stud, Student(2, 'коксакер', 18, 'м', 'Тула', 'Москва')])
print(studs.students)


studs.addStudent(Student(3, 'пиздолис', 18, 'м', 'Пермь', 'Москва'))
print(studs.students)

for student in studs.students:
    print(student.toFileRow())

# studs.saveStudentsToFile('students.txt')

studs2 = StudentGroup()
studs2.getStudentsFromFile('students.txt')
print('\nИз файла:\n')
for student in studs2.students:
    print(student.toFileRow())
studs2.deleteStudent(4)

print('\nУдалили 4-го:\n')
for student in studs2.students:
    print(student.toFileRow())

studs2.printAsTable()

studs2.updateStudent(5, Student(5, 'Сидоров С.С.', 21, 'м', 'Ярославль',
                                'Москва'))
studs2.printAsTable()

studs2.printStudentById(5)
