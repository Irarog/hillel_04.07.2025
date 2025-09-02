class UserLimitExceeded(Exception):
    print("There is more than 10 students in this group.")

class Human:

    def __init__(self, gender: str, age:int, first_name:str, last_name:str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'{self.gender} {self.age} {self.first_name} {self.last_name}'

class Student(Human):

    def __init__(self, gender:str, age:int, first_name:str, last_name:str, record_book:str) -> None:
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self) -> str:
        return f'{self.gender} {self.age} {self.first_name} {self.last_name} {self.record_book}'

class Group(Student):

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

    def find_student(self, last_name:str) -> Student:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self) -> str:
        for student in self.group:
            all_students = f'{student.first_name} {student.last_name} ({student.record_book})\n'
        return f'Number: {self.number}\n{all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!


try:
    for i in range(11):
        st = Student('Male', 20, 'Name', 'Last', 'RB')
        gr.add_student(st)
except UserLimitExceeded as e:
    print(f"Exception: {e}")