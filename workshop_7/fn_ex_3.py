"""
Create a function that will ask user for 2 numbers
print their sum
"""

def sum_two():
    nums = [
        int(input("Num: "))
        for i in range(2)
    ]

    total = 0
    for num in nums:
        total += num
    print(total)

sum_two()
