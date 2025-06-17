student = {
    # key: value pairs
    "name": "Nick",
    "age": 27,
    "grades": [87, 88, 90, 91, 97],
    "pet": "Dog"
}

print(student)

print(student["name"])
print(student["age"])

average_grade = sum(student["grades"]) / len(student["grades"])
print(f"Average Grade: {average_grade}")

student["grades"].append(95)
print(student["grades"])

student["pet"] = "Cat"

print(student)

student.pop("pet")
print(student)

student["car"] = "Tesla Model 3"
print(student)
