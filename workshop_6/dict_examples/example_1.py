person = {
    "name": "Alice",
    "age": 17
}

print(person["name"])
person["name"] = "Alison"
print(person["name"])

person["city"] = "Paris"

print(f"Hello I'm {person['name']} and I'm {person['age']} years old, I'm from city of {person['city']}")

if person["age"] < 18:
    print(f"{person['name']} is Minor")
else:
    print(f"{person['name']} is Adult")


person.pop("age")
if "age" in person:
    print("Yes, age key exists in person dict")
else:
    print("No, age key does not exist in person dict")