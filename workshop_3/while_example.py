# write to code to ask use for input for name and say "Hi {name}" until user inputs stop

# user = input("What's your name? ")
# while user != "stop":
#     print(f"Hi {user}")
#     user = input("What's your name? ")


while True:
    user = input("What's your name? ")
    if user == "stop":
        break

    print(f"Hi {user}")
