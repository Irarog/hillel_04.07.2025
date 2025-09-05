from human import Student
from exceptions import UserLimitExceeded


class Group:

    def __init__(self, number:int) -> None:
        self.number = number
        self.group = set()

    def add_student(self, student:Student) -> None:
        if len(self.group) >= 10:
            raise UserLimitExceeded("There is more than 10 students in this group.")
        self.group.add(student)

    def delete_student(self, last_name:str) -> None:
        student_to_remove = None
        for student in self.group:
            if student.last_name == last_name:
                student_to_remove = student
                break
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name:str) -> Student|None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        all_students = ""
        for student in self.group:
            all_students += f'{student.first_name} {student.last_name} ({student.record_book})\n'
        return f'Number: {self.number}\n{all_students}'

