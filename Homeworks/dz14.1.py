class TooManyStudentsError(Exception):
    """Користувацький виняток: у групі вже 10 студентів"""
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} y.o., {self.gender}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f", Record book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise TooManyStudentsError("Неможливо додати більше 10 студентів у групу!")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(s) for s in self.group)
        return f"Group {self.number}:\n{all_students}"


# ---------------- Тест ----------------
st1 = Student('Male', 20, 'John', 'Smith', 'RB101')
st2 = Student('Female', 22, 'Anna', 'Brown', 'RB102')

gr = Group('PD1')

try:
    # додаємо 11 студентів
    for i in range(1, 12):
        gr.add_student(Student('Male', 18+i, f'Name{i}', f'Last{i}', f'RB{i}'))
        print(f"Студент {i} доданий")
except TooManyStudentsError as e:
    print("Помилка:", e)

print("\nСписок студентів у групі:")
print(gr)