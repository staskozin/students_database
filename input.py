import os
from student import Student
from num_convert import to_int, to_float


def input_int(message, range=None, error=''):
    number = to_int(input(message))
    if range is not None:
        while range_check(range, number):
            print(error)
            number = to_int(input(message))
    return number


def input_float(message, range=None, error=''):
    number = to_float(input(message))
    if range is not None:
        while range_check(range, number):
            print(error)
            number = to_float(input(message))
    return number


def range_check(range, number):
    if range[0] > range[1]:
        range = (range[1], range[0])
    if number < range[0] or number > range[1]:
        return True
    else:
        return False


def input_record_book(message, group):
    record_book = to_int(input(message))
    while group.student_group.is_student_exists(record_book):
        print('Такой номер зачетки уже существует')
        record_book = to_int(input(message))
    return record_book


def input_gender(message, error):
    gender = input(message)
    while gender not in Student.genders:
        print(error)
        gender = input(message)
    return gender


def input_filepath(message, error):
    path = input(message)
    while not os.path.isfile(path):
        print(error)
        path = input(message)
    return path
