def convert_student_to_str(student):
    return (
            'Номер зачетки: ' + str(student.record_book) + '\n' +
            'ФИО: ' + student.name + '\n' +
            'Год обучения: ' + str(student.year_of_study) + '\n' +
            'Средний балл: ' + str(student.avg_grade) + '\n' +
            'Возраст: ' + str(student.age) + '\n' +
            'Пол: ' + student.gender + '\n' +
            'Место рождения: ' + student.birth_place + '\n' +
            'Место проживания: ' + student.living_place + '\n'
    )


def convert_students_to_str(students):
    result = (
        '{:<15}'.format('Номер зачетки') +
        '{:<26}'.format('ФИО') +
        '{:<14}'.format('Год обучения') +
        '{:<14}'.format('Средний балл') +
        '{:<9}'.format('Возраст') +
        '{:<5}'.format('Пол') +
        '{:<17}'.format('Место рождения') +
        '{:<17}'.format('Место проживания') + '\n'
    )
    for student in students:
        result += (
            '{:<15}'.format(student.record_book) +
            '{:<26}'.format(student.name) +
            '{:<14}'.format(student.year_of_study) +
            '{:<14.1f}'.format(student.avg_grade) +
            '{:<9}'.format(student.age) +
            '{:<5}'.format(student.gender) +
            '{:<17}'.format(student.birth_place) +
            '{:<17}'.format(student.living_place) + '\n'
        )
    return result


def convert_students_to_file_str(students):
    result = ''
    for student in students:
        result += (
            str(student.record_book) + ';' +
            student.name + ';' +
            str(student.year_of_study) + ';' +
            str(student.avg_grade) + ';' +
            str(student.age) + ';' +
            student.gender + ';' +
            student.birth_place + ';' +
            student.living_place + '\n'
        )
    return result
