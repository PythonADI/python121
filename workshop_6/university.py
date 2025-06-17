math_101 = [
    {
        "name": "George",
        "grades": [40, 20, 40]
    },
    {
       "name": "Marry",
       "grades": [25, 0, 0]
    },
    {
        "name": "Timothy",
        "grades": [17, 12, 36]
    },
    {
        "name": "George",
        "grades": [32, 18, 37]
    },
    {
        "name": "Nicky",
        "grades": [30, 20, 1]
    }
]
# stundent passes the subject when they have more than 51 total grade

# print(math_101[0]["name"])

for student in math_101:
    total_grade = sum(student["grades"])
    student["pass"] = 51 < total_grade

    if student["pass"]:
        print(f'{student["name"]} Passed Math 101 ({total_grade})')
    else:
        print(f'{student["name"]} Failed Math 101 ({total_grade})')
    # print(student)
