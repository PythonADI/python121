text = "hello there"

for char in text:
    print(char)


# for i in range(len(text)):
#     print(f"{i} | {text[i]}")


for i, char in enumerate(text):
    print(f"{i} | {char}")


num1 = int(input("enter your first number : "))
num2 = int(input("enter your second number :"))
num3 = num1 * num2
text = str(num3)

for i, char in enumerate(text):
    print(f"{i} / {char}")