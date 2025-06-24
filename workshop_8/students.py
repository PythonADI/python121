"""
Create a class thazt will hold following attributes:
- name
- last_name
- gpa
- university

create at least 5 instances / object of this class
"""
import random

class Student:
    def __init__(self, name, last_name, gpa, university):
        self.name = name
        self.last_name = last_name
        self.gpa = gpa
        self.university = university

    def describe(self):
        print(f"Name : {self.name}\nLast_name : {self.last_name}\nGPA : {self.gpa}\nUNI : {self.university}")



data = {
    "names": ["Marry", "George", "John", "Jane", "Jerry"],
    "last_names": ["Doe", "Ford"],
    "universities": ["Harvard", "Brentford", "Standford", "MIT"]
}
students = []

# print(random.randint(0, 100))
# print(names[random.randint(0, len(names) - 1)])
print(random.choice(data["names"]))

for _ in range(10):
    students.append(
        Student(
            random.choice(data["names"]),
            random.choice(data["last_names"]),
            round(random.random() * 3 + 1, 2),
            random.choice(data["universities"])
        )
    )

print(f"we have {len(students)} students")
for student in students:
    print("-" * 100)
    student.describe()


gpas = [student.gpa for student in students]
print(f"AVG GPA is: {round(sum(gpas) / len(gpas), 2)}")
