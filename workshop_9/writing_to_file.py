"""
There are two way to write into a file
Append (a)
Write (w)

they both create a file if it doesn't already exists and write into it

differnece between append and write is that if file already exists append will add newly
written text at the end if it is open write mode then it will re-write and delete old stuff 
"""
import os
name = input("Enter name: ")

with open(".\\workshop_9\\test.txt", "a") as f:
    f.write(name + "\n")

# os.remove(".\\workshop_9\\names.txt")