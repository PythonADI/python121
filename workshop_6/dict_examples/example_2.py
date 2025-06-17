friends = [
    {
        "name": "Marry",
        "age": 25,
    },
    {
        "name": "George",
        "age": 26
    },
    {
        "name": "Alison",
        "age": 24
    },
    {
        "name": "Nicky",
        "age": 25
    }
]

total_age = 0
adult_friend_count = 0

for friend in friends:
    print(f"Hello I'm {friend['name']} and I'm {friend['age']} years old")
    total_age += friend["age"]
    # friend["is_adult"] = friend["age"] > 18
    if friend["age"] > 18:
        adult_friend_count += 1



print(f"Friend group's average age is: {total_age / len(friends)}")
print(f"Firend group consists total of {adult_friend_count} adult(s) and {len(friends) - adult_friend_count} minor(s)")
# print(friends)