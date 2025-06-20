def greet(user = "Annonymous", age = 0):
    # user now has a default value that is equal to "Annonymous"
    # if you don't pass any arguments it will be default value
    print(f"Hello {user}, I'm {age} years old")

greet()
greet("Nick", 27)
greet("Giorgi")
