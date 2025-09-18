from student import Student

class TooManyStudentsError(Exception):
    """Користувацький виняток: у групі вже 10 студентів"""
    pass


class Group:
    def __init__(self, number, max_students=10):
        self.number = number
        self.group = set()
        self.max_students = max_students

    def add_student(self, student: Student):
        if len(self.group) >= self.max_students:
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