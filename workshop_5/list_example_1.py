"""
write a program that will ask user for 10 names and save them to the list
"""

names = []

for i in range(10):
    names.append(input("Enter Name:"))

print(names)
print(f"There are {len(names)} in the list")
