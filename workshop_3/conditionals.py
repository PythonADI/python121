age = int(input("Age: "))

if age < 12:
    print("You are minor")
elif age < 17:
    print("You are teenager")
elif age < 29:
    print("You are young adult!")
else:
    print("You are an adult!")
