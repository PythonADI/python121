num = input("Num: ")
print(num)
s = 0
# for i in range(len(num)):
#     s += int(num[i])

for char in num:
    s += int(char)
print(s)