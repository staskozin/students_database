from num_convert import to_int, to_float


class Student():
    genders = frozenset('мж')

    def __init__(self, record_book, name, year_of_study,
                 avg_grade, age, gender, birth_place, living_place):
        self.set_record_book(record_book)
        self.set_name(name)
        self.set_year_of_study(year_of_study)
        self.set_avg_grade(avg_grade)
        self.set_age(age)
        self.set_gender(gender)
        self.set_birth_place(birth_place)
        self.set_living_place(living_place)

    def set_record_book(self, record_book):
        self.record_book = abs(to_int(record_book))

    def set_name(self, name):
        self.name = str(name)

    def set_year_of_study(self, year_of_study):
        yos = abs(to_int(year_of_study))
        if yos > 6:
            self.year_of_study = 6
        elif yos < 1:
            self.year_of_study = 1
        else:
            self.year_of_study = yos

    def set_avg_grade(self, avg_grade):
        ag = abs(to_float(avg_grade))
        if ag < 1:
            self.avg_grade = 1.0
        elif ag > 5:
            self.avg_grade = 5.0
        else:
            self.avg_grade = ag

    def set_age(self, age):
        self.age = abs(to_int(age))

    def set_gender(self, gender):
        g = str(gender)
        self.gender = g if g in Student.genders else '-'

    def set_birth_place(self, birth_place):
        self.birth_place = str(birth_place)

    def set_living_place(self, living_place):
        self.living_place = str(living_place)
