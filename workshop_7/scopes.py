
def greet_user(user):
    # user is a parameter and shadow global user
    print(f"გამარჯობა {user}")
    print(f"This is global variable {test}")

user = "Nick"
test = 7

greet_user(user)
greet_user("Gela")

