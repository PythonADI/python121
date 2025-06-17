grades = [87, 91, 67, 76, 88]

print(grades)

total_grades = 0
maximum_grade = grades[0]
minimum_grade = grades[0]

for grade in grades:
    total_grades += grade

    if maximum_grade < grade:
        maximum_grade = grade

    if minimum_grade > grade:
        minimum_grade = grade


avg_grade = total_grades / len(grades)
print(f"Average grade is: {avg_grade}")
print(f"Maximum grade is: {maximum_grade}")
print(f"Minimum grade is: {minimum_grade}")
print("-" * 10)
print(f"Average grade is: {sum(grades) / len(grades)}")
print(f"Maximum grade is: {max(grades)}")
print(f"Minimum grade is: {min(grades)}")
