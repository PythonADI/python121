text = input("Enter some string: ")

print("hello"[4])
print("gamarjoba"[8])


print(text[1])
print(len(text))
print(f"First Character is \"{text[0]}\"")
print(f"Last Character is \"{text[len(text) - 1]}\"")


reversed_string = ""
for i in range(len(text) - 1, -1, -1):
    # print(text[i])
    reversed_string += text[i]

print(reversed_string)