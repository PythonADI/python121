class Dog:
    # class definition
    def __init__(self, name, age):
        # constructor function
        # attributres
        self.name = name
        self.age = age


dog1 = {
    "name": "jerry",
    "age": 1
}
dog2 = {
    "NAME": "Lima",
    "age": 4
}
# here we created dog object
dog = Dog("Milo", 1) # instantiation
dog2 = Dog("Fido", 5)

print(dog.name, dog.age)
print(dog2.name, dog2.age)
