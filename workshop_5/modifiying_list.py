temps = [32, 35, 37, 13, 25, 27, 33]

# adding elements at the end
temps.append(39)
print(temps)

temps.append(38)
print(temps)

# removing elements from the end
temps.pop()
print(temps)

temps.pop()
print(temps)

# adding elements anywhere
temps.insert(0, 56)
print(temps)

temps.insert(len(temps), 35)
print(temps)

temps.insert(len(temps) // 2, -7)
print(temps)

# updating elements
temps[0] += 1
print(temps)

temps[len(temps) // 2] = 99
print(temps)
