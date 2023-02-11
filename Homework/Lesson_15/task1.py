# Task 1
# School
# Make a class structure in python representing people at school. Make a base class called Person,
# a class called Student, and another one called Teacher. Try to find as many methods and attributes as you can,
# which belong to different classes, and keep in mind which are common and which are not. For example, the name
# should be a Person attribute, while salary should only be available to the teacher.

class Person:
    def __init__(self, name: str, gender: str, age: int, hair_color: str, height: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.hair_color = hair_color
        self.height = height

    def __repr__(self):
        return self.name


class Student(Person):
    def __init__(self, name, gender, age, hair_color, height, grades: list, attendance: int, parent: Person):
        super().__init__(name, gender, age, hair_color, height)
        self.grades = grades
        self.attendance = attendance
        self.parent = parent

    def get_mark(self, mark: int):
        try:
            self.grades.append(int(mark))
            if not 0 < int(mark) <= 5:
                raise ValueError
            print(f'Added {mark} to {self}\' grades.')
        except (ValueError, TypeError):
            print(f'Sorry, mark needs to be an integer from 1 to 5')

    def duty(self):
        return f"{self.name} is on duty today!"


class Teacher(Person):
    def __init__(self, name, gender, age, hair_color, height, rank):
        super().__init__(name, gender, age, hair_color, height)
        self.rank = rank

    def get_paid(self, total_working_days, basic_hourly_salary=18,  overtime_hours=10):
        total_salary = total_working_days * (basic_hourly_salary * 8) + overtime_hours * 3
        return f"{self.name}'s salary is {total_salary}$ this month."


    def print_rank(self):
        return f"{self.name} is ranked #{self.rank} in school!"


# Creating instances
mikes_mom = Person('Ann', 'Female', 47, 'Brown', 169)
mike = Student('Mike', 'Male', 15, 'Black', 173, [3, 2, 5, 4, 5, 1, 3, 4, 4, 5], 63, mikes_mom)
mrs_jackson = Teacher('Mrs. Jackson', 'Female', 53, 'Blonde', 177, 10)


print(mikes_mom, 'hair color is', mikes_mom.hair_color)
print(mike.name)
print(mike.attendance)
print(mike.duty())
print(mrs_jackson.get_paid(24, overtime_hours=15))
print(mrs_jackson.print_rank())
print(mike.grades)
mike.get_mark(5)
print(mike.grades)