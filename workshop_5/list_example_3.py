"""
ask user for names infinitely 
until user inputs stop.

1. greet every user
    example:
    "hello Nick"
    "hello Gretta"
2. calculate average length of name
3. find longest name
4. find shortest name
5. print every name in reverse


for temp in temps:
    print(f"This is an element of \"temps\" list: {temp}")

temps.append(39)
"""

names = []

while True:
    name = input("Name: ")
    if name == "stop":
        break
    names.append(name)


for user in names:
    print(f"Hello {user}")

total_size = 0
for name in names:
    total_size += len(name)

print(f"Average name length is: {total_size / len(names)}")

longest_name = names[0]
shortest_name = names[0]

for name in names:
    if len(longest_name) < len(name):
        longest_name = name
 
    if len(name) < len(shortest_name):
        shortest_name = name

print(f"longest name is: {longest_name} and has {len(longest_name)} characters")
print(f"shortest name is: {shortest_name} and has {len(shortest_name)} characters")

for name in names:
    reversed_name = ""
    # for i in range(len(name) - 1, -1, -1):
    #     reversed_name += name[i]

    for char in name[::-1]:
        reversed_name += char
    
    print(reversed_name)

