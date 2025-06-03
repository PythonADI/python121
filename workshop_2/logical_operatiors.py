age = 91
# in_range = age > 25 and age < 90
# in_range = 25 < age and age < 90
in_range = 25 < age < 90
# out_of_range = age < 25 or 90 < age
out_of_range = not in_range

print(in_range)
print(out_of_range)

