names = [
    "Nick", "Marry", "Jane", "Jimmy", "Joshua", "Timothy", "Glen", "Jay", "Alexander"
]


shortest_name = names[0]
longest_name = names[0]
total_length = 0

for name in names:
    if len(shortest_name) > len(name):
        shortest_name = name

    if len(longest_name) < len(name):
        longest_name = name

    total_length += len(name)

avg_length = total_length / len(names)
print(f"Shortest name is: \"{shortest_name}\"")
print(f"Longest name is: \"{longest_name}\"")
print(f"Average name is: {avg_length}")
print("-" * 10)

# names_lengths = []
# for name in names:
#     names_lengths.append(len(name))

# list comprehension
names_lengths = [len(name) for name in names]
print(f"Shortest name is: {min(names_lengths)}")
print(f"Longest name is: {max(names_lengths)}")
print(f"Average name is: {sum(names_lengths) / len(names_lengths)}")




