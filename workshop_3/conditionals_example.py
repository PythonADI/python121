name = input("What is your name? ")
age = int(input("How old are you? "))

# 21 < age and age < 29
if name == "Nick" and 21 < age < 29:
    # Indented instructions are called code block
    print("You are lucky")
    print(6 + 8)
    print(6 + 12)
    print(22 + 12)
    print(33 + 81)
    print(126 + 38)
elif name == "Marry" and (age < 21 or 29 < age):
    print("Ho Ho Ho")
else:
    print("Get lost")
