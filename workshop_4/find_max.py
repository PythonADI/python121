
maximum = None

for i in range(5):
    n = float(input("Enter num: "))
    if maximum is None or maximum < n:
        maximum = n

print(maximum)
