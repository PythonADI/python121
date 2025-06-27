from getpass import getpass
class User:
    def __init__(self, username, password, email, age = None, gender = None):
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.gender = gender

    def about(self):
        return (
            f"Username: {self.username}\n"
            f"Password: {self.password}\n"
            f"Email: {self.email}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
        )


def register_user():
    username = input("Username: ")
    password = getpass("Password: ")
    email = input("Email: ")
    age = input("Age (Optional / leave blank): ")
    gender = input("Gender (Optional / leave blank): ")

    # input validation
    if age != "":
        age = int(age)
    else:
        age = None

    if gender == "":
        gender = None
    elif gender.lower() not in ["male", "female", "other"]:
        print("Please choose only from following male / female / other")
        return None

    if len(password) < 8:
        print("Password length should be greater than 8")
        return None

    if "@" not in email:
        print("Invalid email address")
        return None

    return User(username, password, email, age, gender)

user = register_user()

if user is not None:
    print(f"Successfully registered {user.username}")
    print(user.about())

    with open(".\\workshop_9\\users_database.txt", "a") as f:
        f.write(user.about())
else:
    print("Registration Failed!")
