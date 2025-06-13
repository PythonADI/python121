"""
write a program that will ask user for temperature infinitely until user writes quit
then calculate avg temperature
"""
temps = []

while True:
    user_input = input(">>> ")
    if user_input == "quit":
        break

    temps.append(float(user_input))

total = 0

for temp in temps:
    total += temp

print(f"Average temperature is: {total / len(temps)}")