"""
write a function that will take a list as a parameter and return sum of all elements
do not use sum function
"""
def sum_all(*nums, b):
    print(f"{nums = } | {b = }")
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all(1, 7, 9, 8, -5, 10, 100, b="Hello"))
print(sum_all(1, 7, 9, b="GJ"))
