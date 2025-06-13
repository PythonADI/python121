# day_1 = int(input("Enter temperature for day 1: "))
# day_2 = int(input("Enter temperature for day 2: "))
# day_3 = int(input("Enter temperature for day 3: "))
# day_4 = int(input("Enter temperature for day 4: "))
# day_5 = int(input("Enter temperature for day 5: "))
# day_6 = int(input("Enter temperature for day 6: "))


# print((day_1 + day_2 + day_3 + day_4 + day_5) / 5)

temps = [32, 35, 37, 12, 25, 27, 33]

for temp in temps:
    print(f"This is an element of \"temps\" list: {temp}")

for i, temp in enumerate(temps):
    print(f"Day {i + 1}: temperature was: {temp}")

print(f"we recorded total of {len(temps)} days")

# get operator []
print(f"on the first day it was: {temps[0]}")
print(f"on the last day it was: {temps[len(temps) - 1]}")
