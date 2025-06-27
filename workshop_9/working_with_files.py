import random
names = []

# Absolute path indicates path to file from the disk
# Relative path indicates from programs execution to file
with open(".\\workshop_9\\names.txt", "r") as f:
    # with context manager will open then close file automatically
    # print(f.read())
    names = [
        name.strip()
        for name in f.readlines()
    ]

print(random.choice(names))
