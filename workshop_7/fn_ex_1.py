"""
Create a function that will take age as parameter and print if age is less than 18 or not
"""

def is_adult(age):
    if age > 18 :
        print("you are adult")

age = int(input("enter your age"))

is_adult(age)
