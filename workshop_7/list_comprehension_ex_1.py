names = ["John", "Jane", "Doe", "Alice", "Bob"]

names_upper = [names.upper() for names in names]
# first_letter = [char[0].lower() for char in names]
# for name in names:
#     if name.endswith("e"):
#         first_letters.append(name[0].lower())
first_letters = [
    name[0].lower()
    for name in names
    if name.endswith("e")
]

print(first_letters)
print(names_upper)