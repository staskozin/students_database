import unittest


class TestStudentGroup(unittest.TestCase):
    # создать массив объектов класса (количество элементов массива
    # пользователь вводит с клавиатуры)
    def test_create(self):
        pass

    # добавить метод класса – вывод характеристик объектов на экран дисплея
    # в табличном виде
    def test_print_as_table(self):
        pass

    # сохранить сведения об объектах класса в типизированном файле,
    def test_save_to_file(self):
        pass

    # изменить характеристики одного или нескольких объектов класса
    # (с соответствующими изменениями в файле)
    def test_update_students(self):
        pass

    # удалить один или несколько объектов класса в соответствии с критерием
    # (условие вводится пользователем с клавиатуры)
    def test_delete_students(self):
        pass

    # вывести на экран сведения обо всех объектах, хранящихся в файле
    def test_print_from_file(self):
        pass

    # вывести данные (в табличном виде с соответствующим заголовком)
    # об объектах класса, удовлетворяющих некоторому условию
    # (например, список сотрудников в возрасте до 20 лет)
    def test_filter_students(self):
        pass


# описать новый класс объектов на основе существующего (добавить одну
# или несколько новых характеристик)

# создать массив объектов нового класса, показать пользователю
# все объекты класса в табличном виде


if __name__ == '__main__':
    unittest.main()