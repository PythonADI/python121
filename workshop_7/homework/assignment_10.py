current_users = ["Nick", "Nia", "Louie", "Emily", "Kim"]
new_users = ["Tim", "LouIe", "Jenna", "George", "Kim"]


# current_users_lower = []
# for user in current_users: 
#     current_users_lower.append(user.lower())

# list comprehension / generator
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"This {user} is taken! enter a new usename:")
    else:
        print(f"This {user} is available")